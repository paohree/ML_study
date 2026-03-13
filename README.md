# ML Keyword Study

개념 위주로 머신러닝 키워드를 정리하고, 나중에 실습 노트로 이어가기 위한 저장소.

## 공부 방향

- 목표: ML이 뭔지 맥락부터 이해하고, 테이블 데이터 중심으로 실제 흐름을 파악하기
- 우선순위: `ML의 등장 배경 -> 기초 개념 -> 테이블 데이터 전처리 -> 모델 -> 평가`
- 단순 용어 암기가 아니라, 각 개념이 왜 나왔고 어디서 쓰이는지 이해하는 데 집중

## 학습 순서

### 1단계 — ML이란 무엇인가
1. 기존 프로그래밍과 ML의 차이 — 왜 ML이 나왔는가
2. ML이 잘 풀 수 있는 문제 vs 못 푸는 문제
3. 지도학습 / 비지도학습 / 강화학습 — 문제 유형 분류
4. 분류(Classification) vs 회귀(Regression)

### 2단계 — 학습이 어떻게 이루어지는가
5. 훈련 / 검증 / 테스트 세트 분리 — 왜 나누는가
6. 과적합 / 과소적합 — 모델이 왜 망하는가
7. 교차검증 (Cross Validation)
8. 편향-분산 트레이드오프

### 3단계 — 테이블 데이터 중심으로
9. EDA — 데이터를 받으면 가장 먼저 하는 것
10. 전처리 — 결측치, 인코딩, 정규화/표준화, 이상치
11. Feature Engineering
12. 선형 모델 vs 트리 기반 모델 — 뭐가 다른가
13. Random Forest, XGBoost, LightGBM, CatBoost
14. 평가지표 — Accuracy, Precision, Recall, F1, ROC-AUC, RMSE
15. 하이퍼파라미터 튜닝 (Optuna)
16. 모델 해석 (SHAP, Feature Importance)

### 4단계 — 딥러닝은 무엇인가 (가볍게)
17. 신경망 구조 — 레이어, 활성화함수
18. 역전파, 옵티마이저, 학습률
19. CNN / RNN / Transformer — 각각 어떤 문제에 쓰이는가

### 99 — 실습
- 위 개념을 코드로 확인하는 단계

## 폴더 안내

- `01_basics`: ML 등장 배경부터 기초 개념까지
- `02_tabular`: 테이블 데이터 전처리, 모델, 평가
- `03_deep_learning`: 딥러닝 개념 가볍게
- `99_practice`: 실습 노트

## 읽는 순서

1. `01_basics/01_what_is_ml.md`
2. `01_basics/02_learning_types.md`
3. `01_basics/03_train_test_overfit.md`
4. `02_tabular/01_eda_preprocessing.md`
5. `02_tabular/02_models.md`
6. `02_tabular/03_evaluation.md`
7. `03_deep_learning/01_deep_learning_basics.md`
8. `99_practice/01_practice_guide.md`
