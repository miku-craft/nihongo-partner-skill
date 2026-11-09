"""간격 반복 스케줄러 (SM-2 계열 단순판). 상태는 progress/srs.json.

  python3 -I srs.py add v:n5:会う k:日 g:n5:wa     # 새 카드 (오늘 복습 대상)
  python3 -I srs.py due [N]                         # 오늘 복습할 카드, 섞어서 최대 N개 (기본 20)
  python3 -I srs.py grade v:n5:会う good            # again | hard | good | easy
  python3 -I srs.py stats                           # 장수, 밀린 복습, 리치(3번 이상 틀린 카드)
  python3 -I srs.py selftest

카드 id: v:<레벨>:<단어> / k:<한자> / g:<레벨>:<문법id> / kana:<글자>
"""
import json, random, sys
from datetime import date, timedelta
from pathlib import Path

STATE = Path(__file__).parent / "progress/srs.json"
GRADES = ("again", "hard", "good", "easy")
LEECH = 3


def load(path=STATE):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def save(cards, path=STATE):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cards, ensure_ascii=False, indent=1), encoding="utf-8")


def add(cards, ids, today):
    new = [i for i in ids if i not in cards]
    for i in new:
        cards[i] = {"due": today.isoformat(), "ivl": 0, "ease": 2.5, "reps": 0, "lapses": 0}
    return new


def due(cards, today, limit=20):
    ids = [i for i, c in cards.items() if c["due"] <= today.isoformat()]
    random.Random(today.isoformat()).shuffle(ids)  # 섞어서 복습 (interleaving), 같은 날은 같은 순서
    return ids[:limit], len(ids)


def grade(card, g, today):
    if g not in GRADES:
        raise ValueError(f"grade must be one of {GRADES}")
    ivl, ease = card["ivl"], card["ease"]
    if g == "again":
        card["lapses"] += 1
        card["reps"] = 0
        ease, ivl = max(1.3, ease - 0.2), 0  # 오늘 수업 안에서 한 번 더
    elif g == "hard":
        ease, ivl = max(1.3, ease - 0.15), max(1, round(ivl * 1.2))
    elif g == "good":
        ivl = 1 if card["reps"] == 0 else 3 if card["reps"] == 1 else round(ivl * ease)
    else:  # easy
        ease, ivl = ease + 0.15, 4 if card["reps"] == 0 else round(max(ivl, 1) * ease * 1.3)
    if g != "again":
        card["reps"] += 1
    card.update(ivl=ivl, ease=round(ease, 2), due=(today + timedelta(days=ivl)).isoformat())
    return card


def stats(cards, today):
    _, n_due = due(cards, today, 0)
    leeches = [i for i, c in cards.items() if c["lapses"] >= LEECH]
    kinds = {}
    for i in cards:
        kinds[i.split(":")[0]] = kinds.get(i.split(":")[0], 0) + 1
    return {"total": len(cards), "by_kind": kinds, "due_today": n_due, "leeches": leeches}


def selftest():
    t = date(2026, 1, 1)
    cards = {}
    assert add(cards, ["v:n5:会う", "k:日"], t) == ["v:n5:会う", "k:日"]
    assert add(cards, ["k:日"], t) == []  # 중복 등록 무시
    assert due(cards, t)[1] == 2
    c = cards["v:n5:会う"]
    assert grade(c, "good", t)["due"] == "2026-01-02"
    assert grade(c, "good", t)["ivl"] == 3
    assert grade(c, "good", t)["ivl"] == round(3 * 2.5)  # 8일
    grade(c, "again", t)
    assert c["ivl"] == 0 and c["due"] == "2026-01-01" and c["lapses"] == 1 and c["ease"] == 2.3
    for _ in range(2):
        grade(c, "again", t)
    assert stats(cards, t)["leeches"] == ["v:n5:会う"]
    for _ in range(10):
        grade(c, "again", t)
    assert c["ease"] == 1.3  # 하한
    assert due(cards, t, 1)[0] == due(cards, t, 1)[0]  # 같은 날은 같은 순서
    print("selftest ok")


def main(argv):
    today = date.today()
    cmd, args = (argv[0], argv[1:]) if argv else ("stats", [])
    if cmd == "selftest":
        return selftest()
    cards = load()
    if cmd == "add":
        new = add(cards, args, today)
        save(cards)
        print(f"added {len(new)}: {' '.join(new)}")
    elif cmd == "due":
        ids, n = due(cards, today, int(args[0]) if args else 20)
        print(f"due {n} (showing {len(ids)})")
        print("\n".join(ids))
    elif cmd == "grade":
        if args[0] not in cards:
            sys.exit(f"unknown card: {args[0]} (add 먼저)")
        c = grade(cards[args[0]], args[1], today)
        save(cards)
        print(f"{args[0]} → next {c['due']} (ivl {c['ivl']}d, lapses {c['lapses']})")
    elif cmd == "stats":
        print(json.dumps(stats(cards, today), ensure_ascii=False))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
