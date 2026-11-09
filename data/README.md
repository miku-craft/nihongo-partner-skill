# data

`python3 -I data/build.py` 로 `raw/` → 가공 파일을 다시 만든다. 끝에 자체 점검 assert가 있다.

가공 파일(`vocab/`, `kanji/`, `grammar/`)은 저장소에 들어 있어서 수업에는 `raw/`가 필요 없다. 다시 빌드할 때만 아래로 받는다(약 21MB).

```bash
cd data && mkdir -p raw/openjlpt raw/kanjidic2 raw/tatoeba raw/frequencywords
B=https://raw.githubusercontent.com/evanclan/OpenJLPT/HEAD/data/csv
for t in vocab kanji grammar; do for n in 5 4 3 2 1; do curl -sfL "$B/$t-n$n.csv" -o raw/openjlpt/$t-n$n.csv; sleep 1; done; done
curl -sfL http://www.edrdg.org/kanjidic/kanjidic2.xml.gz -o raw/kanjidic2/kanjidic2.xml.gz
T=https://downloads.tatoeba.org/exports/per_language
curl -sfL $T/jpn/jpn-kor_links.tsv.bz2 -o raw/tatoeba/jpn-kor_links.tsv.bz2
curl -sfL $T/jpn/jpn_sentences.tsv.bz2 -o raw/tatoeba/jpn_sentences.tsv.bz2
curl -sfL $T/kor/kor_sentences.tsv.bz2 -o raw/tatoeba/kor_sentences.tsv.bz2
bunzip2 -f raw/tatoeba/*.bz2
curl -sfL https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2016/ja/ja_50k.txt -o raw/frequencywords/ja_50k.txt
```

원본이 갱신되면 건수가 달라져 `build.py` 끝의 assert가 실패할 수 있다. 그때는 OpenJLPT의 `data/json/meta.json` 건수로 assert 값을 고친다.

## 가공 결과

| 경로 | 내용 | 건수 |
|---|---|---|
| `vocab/n5.tsv` ~ `n1.tsv` | JLPT 단어. **레벨 안에서 빈도순 정렬** (`order` 열). 영어 뜻, 원본 예문, 한국어 대역 예문(있을 때만) | 674 / 630 / 1659 / 1778 / 3070 |
| `kanji/n5.tsv` ~ `n1.tsv` | JLPT 한자 + **한국 한자음**(`korean`), 음독, 훈독, 대표 단어. 빈도순 | 84 / 169 / 387 / 398 / 1345 |
| `kanji/ko-on-correspondence.md` | 한국음 받침 → 일본 음독 대응 통계 (데이터에서 직접 계산) | |
| `grammar/n5.tsv` ~ `n1.tsv` | JLPT 문법 패턴, 접속 형태, 예문, 해설 | 81 / 98 / 101 / 123 / 123 |

## 알아 둘 한계

- JLPT는 공식 단어·한자·문법 목록을 공개하지 않는다. 레벨은 Jonathan Waller의 커뮤니티 표준 목록 기준(비공식 근사치).
- `freq_rank`는 영화·드라마 자막 빈도(OpenSubtitles)라 구어에 치우쳐 있고, 활용형 어간 매칭은 휴리스틱이다. 못 찾은 단어는 레벨 중앙값 위치에 둔다.
- 한국어 대역 예문(`ex_ko`)은 Tatoeba 일-한 쌍 2,262개에서 단어가 들어간 가장 짧은 문장을 고른 것. 없는 단어가 많고, 번역 품질은 기여자마다 다르다.
- 뜻은 영어뿐. 한국어 뜻은 수업 중에 선생님이 설명한다.

## 출처와 라이선스

이 폴더의 가공 데이터는 아래 자료를 포함하며 **CC BY-SA 4.0**을 따른다.

| 자료 | 쓴 곳 | 라이선스 |
|---|---|---|
| [OpenJLPT](https://github.com/evanclan/OpenJLPT) v0.3.0 — JMdict·KANJIDIC2(EDRDG), Jonathan Waller의 JLPT 목록, Tatoeba 포함 | 단어·한자·문법 본체 | CC BY-SA 4.0 |
| [KANJIDIC2](https://www.edrdg.org/wiki/KANJIDIC_Project.html) (EDRDG) | 한국 한자음 | CC BY-SA 4.0 ([EDRDG licence](https://www.edrdg.org/edrdg/licence.html)) |
| [Tatoeba](https://tatoeba.org) 일본어·한국어 문장과 연결 | 한국어 대역 예문 | CC BY 2.0 FR |
| [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) ja_50k (OpenSubtitles 2016) | 빈도 순위 | CC BY-SA 4.0 |

Contains data from OpenJLPT (CC BY-SA 4.0), which uses JMdict and KANJIDIC2 (EDRDG), Jonathan Waller's JLPT lists, and Tatoeba.
