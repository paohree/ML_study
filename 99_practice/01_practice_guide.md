# 실습 가이드

## 실습 목표

지금 단계에서는 "성능 대회"보다 아래 목표가 중요하다.

- 데이터 한 장을 읽을 수 있다
- 어떤 컬럼이 feature이고 target인지 구분할 수 있다
- 분류인지 회귀인지 구분할 수 있다
- baseline 모델 하나를 돌려볼 수 있다
- 결과 지표를 읽을 수 있다

## 추천 실습 흐름

1. CSV 불러오기
2. target 컬럼 정하기
3. 숫자형 / 범주형 컬럼 나누기
4. 결측치 확인
5. 간단한 인코딩/전처리
6. train/test split
7. baseline 모델 학습
8. 평가지표 확인

## baseline 모델 추천

### 분류 문제

- Logistic Regression
- Random Forest
- LightGBM 또는 CatBoost

### 회귀 문제

- Linear Regression
- Random Forest Regressor
- LightGBM Regressor

## 초보자 실수

- test 데이터를 먼저 자주 확인함
- 전처리를 train/test에 다르게 적용함
- Accuracy만 보고 판단함
- feature 의미를 모르고 모델만 바꿈
- 튜닝부터 시작함

## 실습 메모 템플릿

아래 형식으로 노트를 남기면 된다.

### 데이터셋 이름

- 문제 유형:
- target:
- 샘플 수:
- 주요 feature:
- 결측치 여부:
- 범주형 컬럼 여부:

### 해본 것

- 어떤 전처리를 했는지
- 어떤 모델을 썼는지
- 어떤 지표를 봤는지

### 느낀 점

- 뭐가 헷갈렸는지
- 어떤 키워드를 더 공부해야 하는지

## 지금 단계에서 충분한 수준

아래를 말할 수 있으면 잘 가고 있다.

- "이 문제는 분류 문제다"
- "이 컬럼은 범주형이라 인코딩이 필요하다"
- "결측치가 있어서 처리해야 한다"
- "Random Forest와 LightGBM은 트리 기반 모델이다"
- "점수가 높아도 leakage가 있을 수 있다"
