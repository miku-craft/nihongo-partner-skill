# 학습 방법론 — 근거와 적용

> 이 문서는 "왜 이렇게 가르치는가"를 정리한다. 실제 진행 순서는 `curriculum.md`, 운영 규칙은 `.claude/skills/miya/SKILL.md`.
> 근거 강도: ★★★ 메타분석·대규모 리뷰에서 반복 확인 / ★★ 연구는 있으나 조건부·소수 연구 / ★ 경험칙·한국어 화자 특화 아이디어
> 출처 표시 중 "(초록 확인)"은 원문 전체가 아니라 초록·2차 인용으로 확인한 것이다. 효과 크기를 인용하기 전에 원문을 다시 확인한다.

## 0. 큰 틀: 네 가닥 균형 ★★

Nation(2007)은 좋은 언어 과정을 네 가닥으로 나누고, 대략 같은 비중을 주라고 권한다.

| 가닥 | 뜻 | 이 스킬에서 |
|---|---|---|
| 의미 중심 입력 | 뜻을 이해하려고 읽고 듣기 | 예문, **짧은 읽기 지문**(N5부터), 외부 음원 숙제 |
| 의미 중심 출력 | 하고 싶은 말을 직접 말하고 쓰기 | 문장 만들기, 단원 목표 출력 |
| 언어 중심 학습 | 단어·문법·발음을 의식적으로 공부 | 새 문법·단어·한자 설명, 복습 카드 |
| 유창성 | 이미 아는 것을 더 빠르고 매끄럽게 | **같은 주제 다시 말하기**, 쉬운 지문 빨리 읽기 |

초안은 언어 중심 학습에 쏠려 있었다. 그래서 N5부터 짧은 지문과 반복 말하기를 넣었다(`curriculum.md`). 텍스트 대화라서 듣기는 직접 못 하고, 외부 음원으로 보충한다(아래 4번).

## 1. 핵심 원칙

### ① 인출 연습: 보지 말고 떠올리게 한다 ★★★
- 다시 읽기보다 스스로 떠올리는 시험이 장기 기억에 훨씬 낫다(testing effect). Dunlosky 외(2013)가 학습 기법 10개를 비교해 "실전 연습 시험"을 효용 **높음**으로 평가했다. 다시 읽기와 밑줄 긋기는 **낮음**이었다.
- L2 단어에서도 플래시카드(떠올린 뒤 정답 확인)가 단어 목록·쓰기·빈칸 채우기보다 효과적이었다는 메타분석이 있다(Webb 외 2020, 초록 확인). 한 단어를 여러 번 떠올리게 하는 게 좋고, Nakata(2013)는 **약 5번의 인출**을 권한다.
- **적용**: 설명은 짧게 하고 곧바로 문제를 낸다. 단어 목록을 보여주고 "외워 오세요"는 하지 않는다. 모든 학습 단위는 질문으로 끝난다. 새 단어는 그날 수업 안에서 형식을 바꿔 2~3번 떠올리게 하고, 나머지는 복습이 맡는다.

### ② 간격 반복: 잊을 만할 때 다시 ★★★
- 같은 횟수를 공부해도 몰아서 하는 것보다 시간 간격을 두는 쪽이 오래 남는다. Dunlosky 외(2013)에서 인출 연습과 함께 유이한 **높음** 등급이다.
- L2 학습만 모은 메타분석(Kim & Webb 2022, 48개 실험)이 있고, 한국인 학습자 150명 실험에서도 간격 학습이 2주 뒤 시험에서 앞섰다. 효과는 **바로 본 시험이 아니라 며칠 뒤 시험에서** 드러난다.
- 간격을 점점 늘리는 방식과 일정한 간격의 차이는 L2 단어 학습에서 크지 않았다(Nakata 2015). **간격을 둔다는 것 자체가 핵심**이고, 정교한 알고리즘은 부차적이다.
- **적용**: `srs.py`의 단순한 SM-2 계열 스케줄러를 쓴다. 매 수업은 **복습이 먼저, 새 내용은 나중**이다. 밀린 복습이 많으면 새 단어를 줄인다.

### ③ 인지 → 재생 순서로 난이도 올리기 ★★
- 처음 형태와 뜻을 연결할 때는 고르기(인지) 형식이 효율적이다. 어느 정도 익으면 직접 떠올려 쓰는(재생) 형식처럼 **힘든 인출이 더 오래 남는다**(Nakata 2013, desirable difficulty; Suzuki, Nakata & DeKeyser 2019).
- **적용**: 단어 하나는 `읽기(일→한) → 고르기 → 한→일로 직접 말하기` 순서로 올라간다. 정답률이 높으면 바로 다음 형식으로 넘어간다.

### ④ 빈도 우선 ★★★
- 영어 기준으로 텍스트 95%를 이해하려면 약 3,000-4,000 단어족, 98%(도움 없이 편하게 읽는 수준)는 문어 8,000-9,000, 구어 6,000-7,000 단어족이 필요하다(Nation 2006). 자주 나오는 단어부터 배우는 것이 투자 대비 효과가 가장 크다.
- **적용**: JLPT 레벨 순서(N5→N1)를 지키되, **레벨 안에서는 실제 사용 빈도순**으로 배운다(`data/vocab/*.tsv`의 `order` 열). 단, 인사말처럼 빈도 데이터에 안 잡히는 생존 표현은 처음에 따로 묶어서 가르친다.

### ⑤ 문법은 명시적으로, 짧게 ★★★
- 규칙을 직접 설명하는 명시적 교수가 예문만 노출하는 암시적 교수보다 효과가 컸다(Norris & Ortega 2000, 49편; Spada & Tomita 2010; Goo 외 2015 갱신판). 단순한 규칙과 복잡한 규칙 모두에서 그랬다.
- 단, 이 연구들의 시험은 대부분 "규칙을 아는지"를 재서, 실제 대화에서 자동으로 쓰는 능력까지 보장하지는 않는다는 비판이 있다. 그래서 설명 뒤에 **의미 있는 출력과 반복 사용**이 꼭 따라와야 한다.
- **적용**: 문법은 한 줄 요약 + 한국어와의 차이 + 예문으로 짧게 설명하고 곧바로 쓰게 한다. 긴 강의는 하지 않는다.

### ⑥ 고쳐 주기: 먼저 스스로 고치게 ★★
- 교정 피드백 자체는 효과가 분명하다(Mackey & Goo 2007; Li 2010, 메타분석). 효과가 나중 시험까지 유지된다.
- 교실 연구를 모은 Lyster & Saito(2010)에서는 정답을 바로 들려주는 **recast보다, 학습자가 스스로 고치게 유도하는 prompt**(힌트, 되묻기, "다시 한번?")의 효과가 더 컸다(초록 확인). 반면 실험실 연구에서는 recast도 잘 듣는다.
- **적용**: 틀리면 바로 정답을 주지 않고 **한 번은 힌트로 스스로 고칠 기회**를 준다(예: "조사를 다시 볼까요?"). 그래도 틀리면 정답과 이유를 한 줄로 주고 같은 유형 한 문제를 더 낸다. 힌트 받고 맞히면 `hard`로 채점한다.

### ⑦ 섞어서 복습하기 ★★
- 같은 유형만 연달아 푸는 것보다 섞으면 구분하는 힘이 생긴다(interleaving). Dunlosky 외(2013)에서 효용 **중간** 등급이다.
- L2 문법 연습에서도 섞은 쪽이 연습 중엔 더 틀리지만 1주 뒤 시험에서 앞섰다(Nakata & Suzuki 2019). **헷갈리는 짝일수록** 효과가 크다는 보고가 있다(Suzuki 외 2022). 말하기 유창성에는 효과가 덜 분명하다.
- **적용**: 복습할 때 단어, 한자, 문법 카드를 섞는다. 아래 2번의 한국어 화자 혼동 짝(は/が, に/で, 자동사/타동사)은 일부러 같이 낸다.

### ⑧ 이해 가능한 입력 + 출력 + 유창성 ★★
- 지금 실력보다 살짝 어려운, 이해할 수 있는 입력을 많이 받아야 습득이 일어난다(Krashen의 입력 가설). 직접 말하고 써 보면서 자기가 모르는 걸 알아차리는 것도 필요하다(Swain의 출력 가설).
- 다독(쉬운 글을 많이 읽기)은 전통적 정독 수업보다 읽기에 효과적이라는 메타분석이 있다(Jeon & Day 2016, 초록 확인). 읽기 속도는 **실력보다 약간 쉬운 글**을 많이 읽을 때 가장 크게 오른다(Beglar & Hunt 2014).
- 같은 내용을 시간을 줄여 가며 세 번 말하는 4/3/2 활동은 **유창성**을 꾸준히 올리지만 정확성은 따로 피드백이 있어야 오른다(Tran & Saito 2021).
- **적용**: 단원이 끝날 때마다(N5·N4) 또는 수업마다(N3~) 배운 단어로만 쓴 짧은 지문을 읽힌다. 단원 목표 출력은 **같은 주제로 세 번** 말하게 하고, 두 번째부터는 힌트 없이 더 짧고 빠르게 하게 한다. 교정은 세 번째가 끝난 뒤 한꺼번에 한다.

### ⑨ 불안 낮추기 ★★★
- 외국어 불안과 성취는 중간 크기의 음의 상관이 있다(Teimouri, Goetze & Plonsky 2019, r ≈ −.36; Botes 외 2020도 비슷).
- **적용**: 틀려도 괜찮은 분위기를 만든다. 사용자가 먼저 일본어로 말하면 틀렸어도 먼저 반가워한다. 다만 **틀린 답을 맞았다고 하지는 않는다**(정확성이 먼저). 미야 캐릭터의 "조심스럽지만 틀린 건 꼭 고친다" 설정이 이 균형을 맡는다.

## 2. 한국어 화자 전용

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
- 한자 학습 연구에서는 이야기를 지어내는 것보다 **부수·부품 지식**이 더 쓸모 있었다는 보고가 있다(Ke 1998, 2차 인용). 그래서 한자 수가 많아지는 N2·N1에서는 같은 음을 내는 부품끼리 묶어 가르친다(예: 青·清·晴·精·静 → セイ).

### 발음: 한국어 화자가 잘 틀리는 곳 ★★
한국어는 유성/무성 대립이 아니라 평음·격음·경음 대립이라서 다음이 반복해서 보고된다.

| 혼동 | 예 | 근거 |
|---|---|---|
| 어두 청음/탁음 (か/が, た/だ) | 金(きん)/銀(ぎん), 天気(てんき)/電気(でんき) | 어두 유성음을 무성으로 내고, 어두 무성음을 유성으로 잘못 듣는다(Kashima & Hashimoto 2008, 미에대 종단 연구) |
| 촉음 유무 (っ) | きて/きって, かこ/かっこ | 모음 사이 무성음을 경음처럼 내서 촉음처럼 들린다. 듣기에서는 촉음을 놓친다(Min 2007, Koshiro 2007) |
| 장음 유무 | おばさん/おばあさん, ここ/こうこう | 한국어에 없는 길이 대립 |

- **적용**: 가나 단계에 위 짝을 **최소대립쌍 퀴즈**로 넣고, 단계 1 이후에도 이런 짝이 나오는 단어는 복습에서 같이 낸다. 텍스트로는 소리를 들려줄 수 없으니, 표기 구분 + 외부 음원으로 듣고 따라 하기를 숙제로 권한다.

### 문법: 한국어 화자가 잘 틀리는 곳 ★★
- 한국어와 어순이 같고 조사 체계가 비슷해서 "한국어 은/는 ≈ は"처럼 대응을 먼저 보여주면 빠르다. 대신 **비슷해서 틀리는 곳**에 시간을 쓴다.
- 한국인 학습자의 구어 코퍼스(KY 코퍼스) 분석에서 격조사 **が·を·で·に** 오용이 많았고, 원인은 모어 간섭과 과잉 일반화였다(조남성, earticle A395599).
- **자동사/타동사** 구분(開く/開ける, 始まる/始める)도 반복해서 틀린다. "타동사는 を"라는 규칙은 예외가 많아 짝으로 외우는 게 낫다(오현정 2010 외).
- 한국어와 어긋나는 대표 예: 「バスに乗る」(버스를 타다), 「友達に会う」(친구를 만나다), 「〜が好きだ」(〜를 좋아하다), 「〜が分かる」(〜를 알다).
- **적용**: 위 항목은 처음 배울 때 "한국어랑 다른 곳"으로 짚고, 복습에서 혼동 짝으로 섞어 낸다.

## 3. 쓰지 않거나 제한적으로만 쓰는 것

| 방법 | 판단 | 이유 |
|---|---|---|
| 다시 읽기, 하이라이트 | 쓰지 않음 | Dunlosky 외(2013) 효용 낮음 |
| 단어 목록 통째로 보기 | 쓰지 않음 | 인출이 없음 |
| 키워드 기억법(발음 연상 이미지) | **안 외워지는 단어(리치)에만** | 효용 낮음 평가(오래 못 감). 3번 이상 틀린 단어에 마지막 수단으로는 쓸모 있음 |
| 정교한 FSRS 알고리즘 | 지금은 안 씀 | 예측 정확도 벤치마크는 있지만, "복습 20~30% 감소" 같은 수치는 검증된 출처를 못 찾았다. 이 규모에선 간격을 두는 것 자체가 핵심. 복습량이 수천 장을 넘으면 교체 검토 |
| 바로 정답 주기(recast만) | 두 번째 시도에서만 | ⑥ 참고. 먼저 스스로 고칠 기회를 준다 |
| 과제 중심 교수(TBLT) 전면 도입 | 단원 목표 출력으로만 | 큰 효과 보고(Bryfonski & McKay 2019, d = 0.93)가 있지만 재분석에서 줄었고(g ≈ 0.61) "과제"의 정의도 불분명하다는 비판이 있다 |

## 4. 텍스트 수업의 한계와 보충

- **듣기·발음**: 대화창은 소리를 낼 수 없다. 섀도잉(들으면서 바로 따라 말하기)은 듣기와 운율에 도움이 된다는 연구가 있지만 대부분 소규모다. 단계 1부터 수업 끝에 "오늘 단어를 외부 음원으로 듣고 따라 하기"를 **선택 숙제**로 권한다.
- **피치 악센트**: 음 높이를 표기로 보여 주는 훈련이 처음 보는 단어에까지 효과가 이어졌다(Hirata 외 2024). 텍스트로도 할 수 있는 방식이라 N4부터 선택 과목으로, 혼동 짝(箸/橋, 雨/飴)부터 높낮이 표기를 보여 준다.
- **AI 대화 상대**: 대화형 챗봇이 L2 학습에 긍정적 효과가 있다는 메타분석이 늘고 있다. 최신 LLM 기반이 가장 큰 추정치를 보였다는 예비 결과가 있지만(Wang 외, 학회 발표) 아직 확정적이지 않다. 이 스킬은 그 장점(언제든 출력·즉시 피드백)을 쓰되, 정확성 규칙으로 약점(그럴듯한 오답)을 막는다.

## 5. 한 수업의 모양 (원칙 → 루틴)

1. **복습** (②⑦): `srs.py due`로 오늘 복습 카드를 꺼내 섞어서 낸다.
2. **새 문법 1개** (⑤): 짧은 설명, 한국어와의 대응·차이, 예문 2~3개.
3. **새 단어 묶음** (④): 빈도순 다음 단어를 예문 속에서 보여준다.
4. **새 한자** (2번): 한국음 → 받침 규칙 → 음독 → 아는 단어.
5. **인출 연습** (①③): 읽기 → 고르기 → 직접 말하기.
6. **출력** (⑥⑧): 오늘 문법과 단어로 사용자가 문장을 만든다. 먼저 스스로 고치게 유도한다.
7. **기록** (②): 새 카드 등록, 채점 결과 반영, `progress.md` 갱신.

단원 끝에는 **읽기 지문 + 목표 출력 3번 반복**(⑧)이 더해진다. 한 번에 20~30분 분량, **짧게 자주**가 길게 가끔보다 낫다(②).

## 참고 자료

- Dunlosky, J. 외 (2013). Improving Students' Learning With Effective Learning Techniques. *Psychological Science in the Public Interest*. — [APS 보도자료](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html)
- Nation, I.S.P. (2006). How large a vocabulary is needed for reading and listening? — [PDF](https://www.wgtn.ac.nz/__data/assets/pdf_file/0018/1626120/2006-How-large-a-vocab.pdf)
- Nation, I.S.P. (2007). The four strands. — [요약 자료(Yamamoto)](https://vuw-web.matrix.squiz.cloud/lals/resources/paul-nations-resources/paul-nations-publications/publications/documents/yamamoto-four-strands.pdf)
- Nakata, T. (2013). Optimising Second Language Vocabulary Learning from Flashcards (박사논문) — [기록](https://ir.wgtn.ac.nz/handle/123456789/29297?show=full)
- Nakata, T. (2015). Effects of expanding and equal spacing on second language vocabulary learning. *SSLA* — [Cambridge](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/effects-of-expanding-and-equal-spacing-on-second-language-vocabulary-learning/D1D796306985C52F9BE7A1200AC50DB9)
- Kim, S. K. & Webb, S. (2022). The effects of spaced practice on second language learning: A meta-analysis. *Language Learning* 72(1). — [관련 학위논문](https://ir.lib.uwo.ca/etd/8600/)
- Nakata, T. & Suzuki, Y. (2019). Mixing grammar exercises facilitates long-term retention. *Modern Language Journal*. — [Nakata 논문 목록](https://scite.ai/authors/tatsuya-nakata-rxJx8w)
- Norris, J. & Ortega, L. (2000) / Spada, N. & Tomita, Y. (2010). 명시적·암시적 교수 메타분석. — [Spada & Tomita 소개](https://www.eas.utoronto.ca/node/790), [비판 논문(MEXTESOL 2023)](https://mextesol.net/journal/public/files/22c2f35b587c8952dc69cf81185f4faf.pdf)
- Lyster, R. & Saito, K. (2010). Oral feedback in classroom SLA: A meta-analysis. *SSLA* 32. — [Lyster, Saito & Sato 2013 리뷰](https://www.scribd.com/document/632285530/LysterSaitoSato2013)
- Teimouri, Y., Goetze, J. & Plonsky, L. (2019). Second language anxiety and achievement: A meta-analysis. *SSLA* 41(2). — [NAU](https://experts.nau.edu/en/publications/second-language-anxiety-and-achievement/)
- Tran, M. N. & Saito, K. (2021). 4/3/2 활동과 유창성·정확성. — [UCL](https://discovery.ucl.ac.uk/10128571/1/LTR2021.pdf)
- Jeon, E. Y. & Day, R. (2016) 다독 메타분석 / Beglar & Hunt (2014). — [JALT 다독 연구(일본어 학습자)](https://jalt-publications.org/content/index.php/jer/article/view/petersonandwarnick)
- Bryfonski, L. & McKay, T. (2019). TBLT implementation and evaluation: A meta-analysis. — [대영도서관 기록](https://eld.bl.uk/catalog/100089188607_0x000001)
- Hirata, Y. 외 (2024). Multimodal training on L2 Japanese pitch accent. *Language and Cognition*. — [Cambridge](https://www.cambridge.org/core/product/AB2195C963F348823C8175220F9F9EA1)
- 한국인 학습자 발음: Kashima & Hashimoto (2008) [J-STAGE](https://www.jstage.jst.go.jp/article/onseikenkyu/12/3/12_KJ00007631967/_article/-char/en), Min (2007) [J-STAGE](https://www.jstage.jst.go.jp/article/onseikenkyu/11/1/11_KJ00007631787/_article/-char/en), Koshiro (2007) [J-STAGE](https://www.jstage.jst.go.jp/article/onseikenkyu/11/1/11_KJ00007631790/_article/-char/en), 미에대 종단 연구 [저장소](https://mie-u.repo.nii.ac.jp/records/6832)
- 한국인 학습자 조사·자타동사 오용: 조남성 [earticle A395599](https://www.earticle.net/Article/A395599), 오현정(2010) [earticle A120273](https://www.earticle.net/Article/A120273), [한양대 학위논문](https://repository.hanyang.ac.kr/handle/20.500.11754/127621)
- 한일 한자음 대응 연구(ㄴ→ン, ㄹ→ツ 등) — [earticle A187936](https://www.earticle.net/Article/A187936), [earticle A355565](https://www.earticle.net/Article/A355565)
- 한자 학습 전략(부수 지식 vs 이야기 기억법) — [Japanedu 리뷰](https://ejournal.upi.edu/index.php/japanedu/article/download/63897/pdf)
- 챗봇과 L2 학습 메타분석 — [Hou & Min 2025, ReCALL](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/31847710516602398819C5E594038E7B/S0958344025100268a.pdf/dialogue-based-computer-assisted-language-learning-systems-for-second-language-speaking-development-a-three-level-meta-analysis.pdf), [Wang 외 "Hype or hope?"](https://research.dial.uclouvain.be/entities/publication/29791a54-111b-40eb-bacb-346494980619)
- FSRS (open-spaced-repetition) — [ts-fsrs](https://open-spaced-repetition.github.io/ts-fsrs), [SM-2와 차이](https://l-m-sherlock.notion.site/What-are-the-main-differences-between-SM-2-and-FSRS-135c250163a180ca9029ea460136254c)
- Krashen, S. (1985). *The Input Hypothesis*. / Swain, M. (1985). Communicative competence: Some roles of comprehensible input and comprehensible output. (원문 미확인, 널리 인용되는 고전)
