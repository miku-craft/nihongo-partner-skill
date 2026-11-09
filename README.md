# nihongo-partner

**현재 초안이며 추후 학습하며 업데이트 예정**

일본어 선생님 캐릭터 미야와 함께 일본어를 배우는 [Claude Code](https://claude.com/claude-code) 스킬.

공개 JLPT 데이터와 학습 연구(인출 연습, 간격 반복, 빈도 우선)를 바탕으로 가나부터 N1까지 한 단계씩 가르친다. 한국어 화자를 위해 한국 한자음으로 일본 음독을 추측하는 규칙(예: 학 → ㄱ받침 → ガク)을 데이터에서 계산해 넣었다.

## 특징

- **이어지는 수업**: 진도와 오답을 파일로 저장해서, 다음 세션에 지난번에 이어서 한다.
- **간격 반복 복습**: 잊을 만할 때 다시 묻는다. 단어·한자·문법 카드를 섞어서 낸다.
- **빈도순 단어**: 같은 JLPT 레벨 안에서도 실제로 자주 쓰는 단어부터.
- **한국 한자음 대응**: `ㄴ→ン 98%`, `ㄹ→ツ 83%`, `ㄱ→ク 73%` 같은 규칙으로 한자 읽기를 연결한다.
- **캐릭터 연출**: 장면에 맞는 표정 이미지 20종과 말투. 단, 문법 설명과 정답 판정에는 연출을 넣지 않는다.

## 시작하기

필요한 것: Claude Code, Python 3

```bash
git clone https://github.com/miku-craft/nihongo-partner.git
```

```bash
cd nihongo-partner && claude
```

Claude Code가 열리면 **"일본어 수업하자"** 또는 `/miya`. 스킬이 `.claude/skills/miya/`에 있어서 이 폴더에서 열어야 잡힌다.

첫 수업이면 레벨 확인 퀴즈부터 한다. 그만하고 싶으면 "그만"이라고 하면 오늘 배운 걸 저장하고 끝낸다.

> 표정 이미지는 Claude Code 데스크톱 앱 대화창에 바로 보인다. 다른 환경에서는 이미지가 안 보일 수 있지만 수업은 그대로 된다.

## 수업 한 번의 흐름

| 단계 | 하는 일 |
|---|---|
| 복습 | 오늘 복습할 카드를 섞어서 문제로 낸다 |
| 새 문법 1개 | 한국어와 같은 점·다른 점 위주로 짧게 |
| 새 단어 8~12개 | 레벨 안에서 사용 빈도가 높은 순서 |
| 새 한자 1~2자 | 한국 한자음 → 받침 규칙 → 일본 음독 |
| 문제 풀기 | 읽기 → 고르기 → 직접 말하기 순으로 어려워진다 |
| 문장 만들기 | 오늘 배운 걸로 직접 한 문장. 틀리면 고친 문장과 이유를 알려 준다 |
| 기록 | 새 카드 등록, 진도 저장 |

- 한 번에 20~30분. 길게 가끔보다 짧게 자주가 낫다.
- 밀린 복습이 30장을 넘으면 그날은 복습만 한다.
- 진도: 가나 → N5(11개 단원) → N4 → N3 → N2 → N1. 하루 한 번이면 N5까지 약 3개월.

## 폴더 구성

| 경로 | 내용 |
|---|---|
| `.claude/skills/miya/SKILL.md` | 수업 운영 규칙 (Claude가 읽는 파일) |
| `character.md` | 미야의 성격, 말투, 이미지 코드 |
| `curriculum.md` | 단계별 범위, N5 단원 순서, 레벨 확인 방법 |
| `methodology.md` | 왜 이렇게 가르치는지 (연구 근거와 출처) |
| `data/` | 단어 7,811 · 한자 2,383 · 문법 526 (출처는 `data/README.md`) |
| `srs.py` | 복습 스케줄러 (표준 라이브러리만 사용) |
| `images/` | 미야 표정 이미지 20종 |
| `clean_images.py` | 이미지를 직접 바꿀 때: NovelAI 원본에서 메타데이터를 지우고 webp로 변환 |
| `progress/` | 내 진도와 복습 기록 (첫 수업 때 생김, git에 안 올라감) |

## 직접 써 볼 수 있는 명령

복습 상태 보기 (전체 카드 수, 오늘 복습할 수, 3번 이상 틀린 카드):

```bash
python3 -I srs.py stats
```

스케줄러 자체 점검:

```bash
python3 -I srs.py selftest
```

데이터 다시 빌드하기 (원본을 먼저 받아야 함, `data/README.md` 참고). 원본 데이터가 틀린 걸 발견하면 `data/build.py`의 `CORRECTIONS`에 추가하고 다시 돌린다.

```bash
python3 -I data/build.py
```

이미지를 바꾸고 싶다면 NovelAI 원본 PNG를 `{코드} 이름.png` 형식으로 `images_src/`에 넣고 실행한다. 코드 목록은 `character.md`. EXIF, PNG 텍스트, 픽셀 끝 비트에 숨은 생성 정보를 지운다.

```bash
uv run --no-project --python 3.12 --with pillow python -I clean_images.py images_src images
```

## 데이터 출처

- [OpenJLPT](https://github.com/evanclan/OpenJLPT): JLPT 단어·한자·문법 (JMdict·KANJIDIC2, Jonathan Waller의 JLPT 목록, Tatoeba 기반)
- [KANJIDIC2](https://www.edrdg.org/wiki/KANJIDIC_Project.html) (EDRDG): 한국 한자음
- [Tatoeba](https://tatoeba.org): 일본어-한국어 대역 예문
- [FrequencyWords](https://github.com/hermitdave/FrequencyWords): 빈도 순위

JLPT는 공식 단어 목록을 공개하지 않는다. 레벨 구분은 커뮤니티 표준 목록 기준의 근사치다.

## 라이선스

- 코드와 문서: [MIT](LICENSE)
- `data/`의 가공 데이터: CC BY-SA 4.0 (출처 표기는 `data/README.md`)
