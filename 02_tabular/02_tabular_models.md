# 테뷸러 데이터 모델

## 어떤 모델부터 봐야 하나?

입문 순서는 보통 아래가 좋다.

1. Linear Regression / Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting 계열
5. XGBoost / LightGBM / CatBoost

테뷸러에서는 딥러닝보다 트리 기반 모델이 기본 전력인 경우가 많다.

## 선형 모델

### Linear Regression

숫자를 예측하는 가장 기본 모델이다.

언제 쓰나?
- 회귀 문제의 baseline
- feature와 target 관계를 단순하게 보고 싶을 때

장점:
- 해석이 쉬움
- 빠름

한계:
- 복잡한 비선형 관계를 잘 못 잡음

### Logistic Regression

이름은 regression이지만 주로 분류에 쓴다.

언제 쓰나?
- 이진 분류 baseline
- 간단하고 해석 가능한 모델이 필요할 때

## Decision Tree

질문을 연속해서 던지는 형태의 모델이다.

예시:
- 나이가 30 이상인가?
- 구매 횟수가 5 이상인가?

장점:
- 직관적
- 비선형 관계를 어느 정도 잡음

단점:
- 하나의 트리는 쉽게 과적합됨

## Random Forest

여러 개의 Decision Tree를 만들어서 결과를 합치는 방식이다.

장점:
- 단일 트리보다 안정적
- 성능이 괜찮고 해석도 어느 정도 가능

단점:
- 부스팅 계열보다 성능이 밀릴 때가 많음

## Boosting 계열

이전 모델이 틀린 부분을 다음 모델이 보완하는 방식이다.

대표:
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

테뷸러 대회나 실무에서 매우 자주 등장한다.

## XGBoost

아주 유명한 부스팅 라이브러리다.

특징:
- 성능이 강력함
- 하이퍼파라미터가 비교적 많음
- 안정적으로 baseline 이상이 잘 나오는 편

## LightGBM

속도와 성능 때문에 많이 쓰인다.

특징:
- 학습이 빠름
- 큰 데이터에서 유리한 경우가 많음
- 범주형 처리도 어느 정도 가능

## CatBoost

범주형 feature가 많은 테뷸러 데이터에서 특히 자주 언급된다.

특징:
- 범주형 처리에 강점
- 전처리가 상대적으로 편한 편
- 초보자에게도 써볼 가치가 큼

## 하이퍼파라미터 튜닝

모델 내부 설정값을 조정하는 과정이다.

예시:
- 트리 깊이
- 학습률
- 트리 개수
- 최소 샘플 수

대표 방식:
- Grid Search
- Random Search
- Optuna

주의:
- 튜닝 전에 baseline부터 만들어야 한다
- 튜닝만으로 모든 문제가 해결되진 않는다

## 모델 해석

### Feature Importance

어떤 feature가 예측에 많이 기여했는지 보여준다.

### SHAP

개별 예측에서 각 feature가 어떤 방향으로 영향을 줬는지 더 자세히 볼 수 있다.

실무에서는 "왜 이렇게 예측했는가"를 설명할 때 자주 쓰인다.

## 입문자 결론

- 처음부터 딥러닝 아키텍처에 집착할 필요 없다
- 테뷸러는 트리 기반 모델부터 보는 게 맞다
- `Random Forest -> XGBoost / LightGBM / CatBoost` 흐름을 익히면 된다
- 좋은 점수를 내려면 모델보다 데이터 이해가 먼저다
