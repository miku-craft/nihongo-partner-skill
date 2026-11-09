# 커리큘럼

> 데이터: `data/` (출처는 `data/README.md`). 근거: `methodology.md`.
> 문법 항목은 `data/grammar/n*.tsv`의 `id`로 적는다. 단어와 한자는 각 TSV의 순서(빈도순)를 따른다.

## 전체 지도

| 단계 | 범위 | 문법 | 단어 | 한자 | 수업 수(대략) |
|---|---|---|---|---|---|
| 0 | 히라가나·가타카나 + 생존 표현 | — | 생존 표현 12개 | — | 6~8 |
| 1 | N5 | 81 | 674 | 84 | 약 80 |
| 2 | N4 | 98 | 630 | 169 | 약 95 |
| 3 | N3 | 101 | 1,659 | 387 | 약 120 |
| 4 | N2 | 123 | 1,778 | 398 | 약 140 |
| 5 | N1 | 123 | 3,070 | 1,345 | 약 200 |

- **수업 1회 = 문법 1개 + 새 단어 약 8~12개 + 새 한자 1~3개 + 복습.** 20~30분.
- 하루 1회면 N5는 약 3개월, N4는 약 3개월 더. 빠르게 가고 싶으면 하루 2회까지. 대신 **밀린 복습이 30장을 넘으면 그날은 새 내용 없이 복습만** 한다.
- 레벨은 Waller의 비공식 JLPT 목록 기준이다. 시험 범위와 완전히 같지는 않다.

## 단계 0 — 가나 (6~8회)

| 회차 | 내용 |
|---|---|
| 0-1 | 히라가나 あ행~さ행 (15자) + 생존 표현: こんにちは, ありがとう, すみません |
| 0-2 | た행~は행 (15자) + はじめまして, どうぞよろしく |
| 0-3 | ま행~ん (16자) + お願いします, いただきます, ごちそうさま |
| 0-4 | 탁음·반탁음(が·ざ·だ·ば·ぱ행) + ごめんなさい, はい, いいえ |
| 0-5 | 요음(きゃ), 촉음(っ), 장음 + 단어 읽기 연습 (N5 단어 앞부분) |
| 0-6~8 | 가타카나 (같은 순서로 압축) + 외래어 읽기(N5 단어 중 가타카나 단어) |

- 가나는 한 회차 끝마다 **읽기 퀴즈 10문제**. 90% 넘으면 다음으로.
- 로마자는 단계 0에서만 쓴다. 단계 1부터는 쓰지 않는다.

## 단계 1 — N5 단원 (가르치는 순서)

| 단원 | 주제 | 문법 id (이 순서대로) | 목표 출력 |
|---|---|---|---|
| 1 | 명사 문장 | desu, wa, ka-question, de-wa-arimasen-ja-nai, no, mo, kore-sore-are-dore, kono-sono-ano-dono, koko-soko-asoko-doko | 자기소개 3문장 |
| 2 | 있다·없다 | ga-aru-ga-iru, ni-location, ga-subject, ya, to-and | 내 방에 있는 것 말하기 |
| 3 | 동사 ます형 | masu, masen, mashita, masen-deshita, o, de-place, ni-time, e, ni-destination, kara-from, made, de-means, to-with, goro | 어제 한 일 말하기 |
| 4 | 형용사 | ku-nai-katta-ku-nakatta, na-na-adjective, deshita, ga-suki-ga-kirai, ga-jouzu-ga-heta, kute-de, amari-nai, zenzen-nai | 좋아하는 것 소개 |
| 5 | 부탁·희망·권유 | o-kudasai, tai, ga-hoshii, mashou, mashou-ka, masen-ka, ni-iku, ne, yo | 가게에서 주문하기 |
| 6 | 비교·정도 | yori, no-hou-ga-yori, to-to-dochira-ga, no-naka-de-ga-ichiban, ka-or, dake, kurai-gurai | 두 가지 비교하기 |
| 7 | 보통형 | da, nai, ta | 반말로 짧게 말하기 |
| 8 | て형 | te, te-kudasai, te-iru, te-kara, te-mo-ii, te-wa-ikenai, naide-kudasai, nakereba-naranai-nakute-wa-ikenai, nakute-mo-ii | 규칙 설명하기 |
| 9 | 시간·경험 | ta-koto-ga-aru, mae-ni, ato-de, tari-tari-suru, nagara, mou-ta, mada-te-inai | 경험 말하기 |
| 10 | 이유·변화·추측 | kara-reason, ga-but, ku-naru-ni-naru, ni-suru, deshou, ni-frequency, ni-indirect-object | 이유 붙여 말하기 |
| 11 | 마무리 | nani-mo-nai-dare-mo-nai, nani-ka-dare-ka-doko-ka, to-iu-named | N5 종합 대화 |

- 단원 7(보통형)에서 **동사 3그룹 활용 규칙**(5단·1단·불규칙)을 정식으로 다룬다. 단원 3에서는 ます형만 덩어리로 익힌다.
- 단원 하나가 끝나면 **목표 출력**을 사용자가 직접 해 보고, 통과해야 다음 단원으로 간다(수치 + 사건 게이트).
- 단어는 `data/vocab/n5.tsv`의 빈도순으로 가져오되, 그날 문법 예문에 필요한 단어는 순서를 앞당겨 쓴다.
- 한자는 단계 1부터 `data/kanji/n5.tsv` 순서로 하루 1~2자. 반드시 **한국음 → 받침 규칙 → 음독 → 그 한자가 들어간 N5 단어** 순서로 연결한다.

## 단계 2~5 — N4 이후

- 문법은 `data/grammar/n4.tsv` 등 **파일 순서대로** 가르친다(N4 이후는 파일이 대체로 쉬운 것부터 정렬돼 있다). 단, 아직 안 배운 활용형이 필요하면 그 활용형을 먼저 한다.
  - N4에서 꼭 지킬 선행 관계: `eru-rareru-potential`(가능형) → `reru-rareru-passive`(수동) → `seru-saseru`(사역) → `serareru-saserareru`(사역수동). `sonkeigo`·`kenjougo`는 N4 문법 후반부에 둔다.
- 단어·한자 수가 커지므로 N3부터는 **하루 새 단어 15개**를 기본으로 한다(복습량을 보고 조절).
- N3부터는 수업마다 짧은 읽기 지문(선생님이 그 레벨 단어로 작성, 3~5문장)을 하나씩 넣는다. 이해 가능한 입력을 늘리는 단계다.

## 레벨 확인 (첫 수업)

1. 히라가나 읽기 5문제 → 하나라도 막히면 단계 0부터.
2. N5 문법 3문제(は/が, ます형 과거, て형) → 다 맞으면 N4 확인 3문제.
3. 틀린 첫 지점의 단원부터 시작한다. 이미 아는 단원의 단어는 `srs.py add`로 등록만 하고 복습에서 확인한다.
