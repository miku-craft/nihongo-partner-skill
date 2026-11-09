# 학습 방법론 — 근거와 적용

> 이 문서는 "왜 이렇게 가르치는가"를 정리한다. 실제 진행 순서는 `curriculum.md`, 운영 규칙은 `.claude/skills/miya/SKILL.md`.
> 근거 강도: ★★★ 메타분석·대규모 리뷰에서 반복 확인 / ★★ 연구는 있으나 조건부 / ★ 경험칙·한국어 화자 특화 아이디어

## 1. 핵심 원칙 6가지

### ① 인출 연습: 보지 말고 떠올리게 한다 ★★★
- 다시 읽기보다 스스로 떠올리는 시험이 장기 기억에 훨씬 낫다(testing effect). Dunlosky 외(2013)가 학습 기법 10개를 비교해 "실전 연습 시험"을 효용 **높음**으로 평가했다. 다시 읽기와 밑줄 긋기는 **낮음**이었다.
- **적용**: 설명은 짧게 하고 곧바로 문제를 낸다. 단어 목록을 보여주고 "외워 오세요"는 하지 않는다. 모든 학습 단위는 질문으로 끝난다.

### ② 간격 반복: 잊을 만할 때 다시 ★★★
- 같은 횟수를 공부해도 몰아서 하는 것보다 시간 간격을 두는 쪽이 오래 남는다(distributed practice). Dunlosky 외(2013)에서 인출 연습과 함께 유이한 **높음** 등급이다.
- 간격을 점점 늘리는 방식과 일정한 간격의 차이는 L2 단어 학습에서 크지 않았다(Nakata 2015, 리뷰). **간격을 둔다는 것 자체가 핵심**이고, 정교한 알고리즘은 부차적이다.
- **적용**: `srs.py`의 단순한 SM-2 계열 스케줄러를 쓴다. 매 수업은 **복습이 먼저, 새 내용은 나중**이다. 밀린 복습이 많으면 새 단어를 줄인다.

### ③ 인지 → 재생 순서로 난이도 올리기 ★★
- 처음 형태와 뜻을 연결할 때는 고르기(인지) 형식이 효율적이다. 어느 정도 익으면 직접 떠올려 쓰는(재생) 형식처럼 **힘든 인출이 더 오래 남는다**(Nakata 2013 학위논문, desirable difficulty).
- **적용**: 단어 하나는 `읽기(일→한) → 고르기 → 한→일로 직접 말하기` 순서로 올라간다. 정답률이 높으면 바로 다음 형식으로 넘어간다.

### ④ 빈도 우선 ★★★
- 영어 기준으로 텍스트 95%를 이해하려면 약 3,000~4,000 단어족, 98%(도움 없이 편하게 읽는 수준)는 문어 8,000~9,000, 구어 6,000~7,000 단어족이 필요하다(Nation 2006). 자주 나오는 단어부터 배우는 것이 투자 대비 효과가 가장 크다.
- **적용**: JLPT 레벨 순서(N5→N1)를 지키되, **레벨 안에서는 실제 사용 빈도순**으로 배운다(`data/vocab/*.tsv`의 `order` 열). 단, 인사말처럼 빈도 데이터에 안 잡히는 생존 표현은 처음에 따로 묶어서 가르친다.

### ⑤ 이해 가능한 입력 + 출력 ★★
- 지금 실력보다 살짝 어려운, 이해할 수 있는 입력을 많이 받아야 습득이 일어난다(Krashen의 입력 가설). 직접 말하고 써 보면서 자기가 모르는 걸 알아차리는 것도 필요하다(Swain의 출력 가설).
- **적용**: 단어는 예문 속에서 보여준다. 표기 단계(로마자 → 후리가나 → 없음)를 사용자 실력에 맞춰 걷어 낸다. 매 수업에 **사용자가 직접 문장을 만드는 단계**가 있다. 틀린 문장은 고친 형태로 다시 들려준다(recast).

### ⑥ 섞어서 복습하기 ★★
- 같은 유형만 연달아 푸는 것보다 유형을 섞으면 구분하는 힘이 생긴다(interleaving). Dunlosky 외(2013)에서 효용 **중간** 등급이다.
- **적용**: 복습할 때 단어, 한자, 문법 카드를 섞는다. は/が, に/で처럼 헷갈리는 짝은 일부러 같이 낸다.

## 2. 한국어 화자 전용 가속 장치

### 한자음 대응 규칙 ★ (데이터로 확인)
일본 한자어 대부분은 음독 조합이고, 한국 한자어와 뿌리가 같다. **한국 한자음의 받침으로 일본 음독의 끝소리를 높은 확률로 예측할 수 있다.** `data/build.py`가 JLPT 한자 2,383자의 KANJIDIC2 한국음과 음독을 직접 세서 만든 표다(`data/kanji/ko-on-correspondence.md`):

| 한국음 받침 | 일본 음독 끝소리 | 예 |
|---|---|---|
| ㄴ | ン 98% | 安(안) アン, 新(신) シン |
| ㅁ | ン 98% | 心(심) シン, 三(삼) サン |
| ㄹ | ツ 83%, チ 11% | 日(일) ニチ·ジツ, 月(월) ゲツ |
| ㄱ | ク 73%, キ 20% | 学(학) ガク, 国(국) コク |
| ㅇ | ウ 73%, イ 18% | 東(동) トウ, 生(생) セイ |
| ㅂ | ウ 68% | 法(법) ホウ, 合(합) ゴウ |

- 한국어 논문들도 같은 경향을 보고한다(ㄴ→ン, ㄹ→ツ, ㅇ→長音 등). 이 표는 그 결과를 이 데이터에서 다시 확인한 것이다.
- **적용**: 한자를 배울 때 `한국음 → 받침 규칙 → 음독` 순서로 연결한다. 例) 학생 → 学生 → がくせい. 처음 보는 한자어도 읽는 법을 추측해 보게 하는 문제를 낸다.
- 한국어와 어순이 같고 조사 체계가 비슷하다. 문법 설명에서 "한국어 은/는 ≈ は"처럼 대응을 먼저 보여주고, **다른 점**(が의 쓰임, 존경·겸양 체계)에 시간을 쓴다.

## 3. 쓰지 않거나 제한적으로만 쓰는 것

| 방법 | 판단 | 이유 |
|---|---|---|
| 다시 읽기, 하이라이트 | 쓰지 않음 | Dunlosky 외(2013) 효용 낮음 |
| 단어 목록 통째로 보기 | 쓰지 않음 | 인출이 없음 |
| 키워드 기억법(발음 연상 이미지) | **안 외워지는 단어(리치)에만** | 효용 낮음 평가(오래 못 감, 적용 범위 좁음). 단, 3번 이상 틀린 단어에 마지막 수단으로는 쓸모 있음 |
| 정교한 FSRS 알고리즘 | 지금은 안 씀 | SM-2보다 예측력이 좋다는 보고가 있지만(개발자 자체 벤치마크), 이 규모에선 간격을 두는 것 자체가 핵심. 복습량이 수천 장을 넘으면 교체 검토 |
| 피치 악센트 | 나중에 | 초급 의사소통엔 우선순위 낮음. N4 이후 선택 과목 |

## 4. 한 수업의 모양 (원칙 → 루틴)

1. **복습** (원칙 ②⑥): `srs.py due`로 오늘 복습 카드를 꺼내 섞어서 낸다.
2. **새 문법 1개** (원칙 ⑤): 짧은 설명, 한국어와의 대응·차이, 예문 2~3개.
3. **새 단어 묶음** (원칙 ④): 빈도순 다음 단어 5~10개를 예문 속에서 보여준다.
4. **인출 연습** (원칙 ①③): 읽기 → 고르기 → 직접 만들기.
5. **출력** (원칙 ⑤): 오늘 문법과 단어로 사용자가 문장을 하나 만든다.
6. **기록** (원칙 ②): 새 카드 등록, 채점 결과 반영, `progress.md` 갱신.

한 번에 20~30분 분량, **짧게 자주**가 길게 가끔보다 낫다(원칙 ②).

## 참고 자료

- Dunlosky, J. 외 (2013). Improving Students' Learning With Effective Learning Techniques. *Psychological Science in the Public Interest*. — [APS 보도자료](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html)
- Nation, I.S.P. (2006). How large a vocabulary is needed for reading and listening? — [PDF](https://www.wgtn.ac.nz/__data/assets/pdf_file/0018/1626120/2006-How-large-a-vocab.pdf)
- Nakata, T. (2013). Optimising Second Language Vocabulary Learning from Flashcards (박사논문) — [기록](https://ir.wgtn.ac.nz/handle/123456789/29297?show=full)
- Nakata, T. (2015). Effects of expanding and equal spacing on second language vocabulary learning. *SSLA* — [Cambridge](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/effects-of-expanding-and-equal-spacing-on-second-language-vocabulary-learning/D1D796306985C52F9BE7A1200AC50DB9)
- 한일 한자음 대응 연구(ㄴ→ン, ㄹ→ツ 등) — [earticle A187936](https://www.earticle.net/Article/A187936), [earticle A355565](https://www.earticle.net/Article/A355565)
- FSRS (open-spaced-repetition) — [ts-fsrs](https://open-spaced-repetition.github.io/ts-fsrs)
- Krashen, S. (1985). *The Input Hypothesis*. / Swain, M. (1985). Communicative competence: Some roles of comprehensible input and comprehensible output. (원문 미확인, 널리 인용되는 고전)
