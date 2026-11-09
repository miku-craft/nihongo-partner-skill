"""raw/ 데이터를 스킬이 바로 읽을 TSV로 가공한다. 실행: python3 -I data/build.py"""
import csv, gzip, re, xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

D = Path(__file__).parent
RAW = D / "raw"
LEVELS = ["n5", "n4", "n3", "n2", "n1"]


def read_csv(p):
    with open(p, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_tsv(p, header, rows):
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


# --- 빈도 (OpenSubtitles 2016, 형태소가 활용형 단위로 쪼개져 있음) ---
freq = {}
for i, line in enumerate(open(RAW / "frequencywords/ja_50k.txt", encoding="utf-8")):
    freq.setdefault(line.split()[0], i + 1)

# 동사·형용사는 사전형이 리스트에 거의 없어서 자주 나오는 활용 어간으로 찾는다.
# shortcut: 휴리스틱 매칭. 짧은 어간은 다른 단어와 겹칠 수 있음 → 정확히 하려면 MeCab 기반 빈도로 교체.
STEM_TAIL = {"v5u": "っ", "v5t": "っ", "v5r": "っ", "v5k": "い", "v5g": "い", "v5s": "し",
             "v5m": "ん", "v5b": "ん", "v5n": "ん", "v5k-s": "っ", "v5r-i": "っ", "v5aru": "っ"}


def has_kanji(s):
    return any("一" <= c <= "鿿" for c in s)


def candidates(word, reading, pos):
    out = [word, reading]
    tags = pos.replace(" ", "").split(";")
    if word[:1] in "おご" and len(word) > 2 and has_kanji(word):
        out.append(word[1:])  # お金 → 金 (토크나이저가 접두어 お를 떼어 냄)
    # 어간은 표기 기준으로만 만든다. 히라가나 읽기로 만든 어간(かっ, たっ)은 다른 단어와 겹친다.
    for base in [word]:
        if len(base) < 2:
            continue
        stem = base[:-1]
        if "adj-i" in tags and has_kanji(stem):
            out.append(stem)  # 青い → 青 (형용사가 青 + い 로 쪼개져 있음)
        if "v1" in tags:
            out.append(stem)
        for t in tags:
            if t in STEM_TAIL:
                out += [stem + STEM_TAIL[t]]
            if t.startswith("v5") and t != "v5r-i":
                out.append(base[:-1] + {"u": "い", "t": "ち", "r": "り", "k": "き", "g": "ぎ",
                                         "s": "し", "m": "み", "b": "び", "n": "に"}.get(t[2:3], ""))
        if "adj-i" in tags:
            out += [stem + "く", stem + "かっ"]  # 맨 어간은 から(辛い) 같은 조사와 겹쳐서 제외
        if "vs" in tags or "vs-i" in tags:
            out.append(base)
    return [c for c in out if c and (len(c) >= 2 or c == word or has_kanji(c))]


def rank_of(r):
    ranks = [freq[c] for c in candidates(r["word"], r["reading"], r["pos"]) if c in freq]
    return min(ranks) if ranks else None


# --- Tatoeba 일본어-한국어 대역 ---
jpn = {}
for line in open(RAW / "tatoeba/jpn_sentences.tsv", encoding="utf-8"):
    i, _, s = line.rstrip("\n").split("\t", 2)
    jpn[i] = s
kor = {}
for line in open(RAW / "tatoeba/kor_sentences.tsv", encoding="utf-8"):
    i, _, s = line.rstrip("\n").split("\t", 2)
    kor[i] = s
pairs = []
for line in open(RAW / "tatoeba/jpn-kor_links.tsv", encoding="utf-8"):
    a, b = line.split()
    if a in jpn and b in kor:
        pairs.append((jpn[a], kor[b]))
pairs.sort(key=lambda p: len(p[0]))  # 짧은 문장 우선 = 초보자용


def ko_example(r):
    if len(r["word"]) < 2:
        return "", ""  # 한 글자는 다른 단어 속에 묻혀 읽기가 달라짐(人 → 韓国人). 원본 영어 예문만 쓴다.
    keys = [r["word"]]
    if len(r["word"]) >= 3:
        keys.append(r["word"][:-1])  # 활용형 대응
    for ja, ko in pairs:
        if any(k in ja for k in keys):
            return ja, ko
    return "", ""


# --- 단어 ---
# 원본 데이터 보정: (레벨, 단어, 원래 읽기) → 바꿀 필드. 수업 중 이상한 항목을 발견하면 여기에 추가한다.
CORRECTIONS = {
    ("n5", "私", "わたくし"): {"reading": "わたし", "romaji": "watashi",
                             "meanings": "I; me (わたくし is the humble/formal reading)"},
}

vocab_total = 0
for lv in LEVELS:
    rows = read_csv(RAW / f"openjlpt/vocab-{lv}.csv")
    for r in rows:
        r.update(CORRECTIONS.get((lv, r["word"], r["reading"]), {}))
        r["_rank"] = rank_of(r)
    # 빈도순. 못 찾은 단어(주로 すみません·お金 같은 복합어·인사말)는 맨 뒤로 밀리지 않게 레벨 중앙값에 둔다.
    ranked = sorted(r["_rank"] for r in rows if r["_rank"])
    mid = ranked[len(ranked) // 2]
    rows.sort(key=lambda r: r["_rank"] or mid)
    out = []
    for n, r in enumerate(rows, 1):
        ja_ko, ko = ko_example(r)
        out.append([n, r["word"], r["reading"], r["meanings"], r["pos"], r["_rank"] or "",
                    r["example_ja"], r["example_en"], ja_ko, ko])
    write_tsv(D / f"vocab/{lv}.tsv",
              ["order", "word", "reading", "meaning_en", "pos", "freq_rank",
               "ex_ja", "ex_en", "ex_ja_kor", "ex_ko"], out)
    vocab_total += len(out)

# --- 한자 + 한국 한자음 ---
korean = {}
root = ET.parse(gzip.open(RAW / "kanjidic2/kanjidic2.xml.gz"))
for ch in root.iter("character"):
    k = [x.text for x in ch.iter("reading") if x.get("r_type") == "korean_h"]
    if k:
        korean[ch.findtext("literal")] = k

kanji_total = 0
corr = defaultdict(Counter)  # 받침 → 음독 끝소리 통계
BATCHIM = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"


def batchim(h):
    code = ord(h[-1]) - 0xAC00
    if not 0 <= code < 11172:
        return "?"
    j = code % 28
    return "없음" if j == 0 else BATCHIM[j - 1]


for lv in LEVELS:
    rows = read_csv(RAW / f"openjlpt/kanji-{lv}.csv")
    rows.sort(key=lambda r: int(r["freq"]) if r["freq"] else 99999)
    out = []
    for r in rows:
        ko = korean.get(r["character"], [])
        out.append([r["character"], "; ".join(ko), r["onyomi"], r["kunyomi"], r["meanings"],
                    r["strokes"], r["freq"], r["words"]])
        ons = [o.strip() for o in r["onyomi"].split(";") if o.strip()]
        if len(ko) == 1 and ons:  # 한국음이 하나인 글자만 통계에 사용 (모호성 제거)
            for o in ons:
                corr[batchim(ko[0])][o[-1] if o[-1] in "クキツチンウイ" else "(모음)"] += 1
    write_tsv(D / f"kanji/{lv}.tsv",
              ["kanji", "korean", "onyomi", "kunyomi", "meaning_en", "strokes", "freq", "words"], out)
    kanji_total += len(out)

# 받침 대응표 (JLPT 한자 전체 기준, 데이터에서 직접 계산)
lines = ["# 한국 한자음 받침 → 일본 음독 끝소리 (JLPT 한자에서 계산)", "",
         "`build.py`가 KANJIDIC2의 한국음(korean_h)과 음독(ja_on)으로 직접 센 값. 한국음이 하나인 한자만 사용.", "",
         "| 받침 | 음독 끝소리 분포 (상위 3) | 표본 |", "|---|---|---|"]
for b in ["없음", "ㄱ", "ㄴ", "ㄹ", "ㅁ", "ㅂ", "ㅇ"]:
    c = corr[b]
    tot = sum(c.values())
    top = ", ".join(f"{k} {v * 100 // tot}%" for k, v in c.most_common(3))
    lines.append(f"| {b} | {top} | {tot} |")
(D / "kanji/ko-on-correspondence.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

# --- 문법 (원본 순서 유지, TSV로만 변환) ---
grammar_total = 0
for lv in LEVELS:
    rows = read_csv(RAW / f"openjlpt/grammar-{lv}.csv")
    write_tsv(D / f"grammar/{lv}.tsv",
              ["id", "pattern", "meaning_en", "formation", "ex_ja", "ex_en", "notes"],
              [[r["id"], r["pattern"], r["meaning"], r["formation"], r["example_ja"],
                r["example_en"], r["notes"]] for r in rows])
    grammar_total += len(rows)

# --- 자체 점검: OpenJLPT meta 수치와 일치해야 함 ---
assert (vocab_total, kanji_total, grammar_total) == (7811, 2383, 526), (vocab_total, kanji_total, grammar_total)
assert corr["ㄴ"].most_common(1)[0][0] == "ン", corr["ㄴ"]  # ㄴ받침 → ン 은 알려진 규칙
assert corr["ㄹ"].most_common(1)[0][0] in "ツチ", corr["ㄹ"]  # ㄹ받침 → ツ/チ
print(f"ok: vocab {vocab_total}, kanji {kanji_total}, grammar {grammar_total}, ko-jp pairs {len(pairs)}")
