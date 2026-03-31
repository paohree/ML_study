# 빅데이터분석기사 실기 — 개요 및 준비 그림

---

## 시험 구성 (180분)

| 유형 | 문제 수 | 배점 | 핵심 |
|---|---|---|---|
| **작업형 1형** | 3문제 | 각 10점 (30점) | pandas 전처리, 값 추출 |
| **작업형 2형** | 1문제 | 40점 | ML 모델링 템플릿 |
| **작업형 3형** | 2문제 | 각 15점 (30점) | 가설검정, 통계분석 |

- 합격선: **60점 이상**
- 과락 없음 → **1형(30) + 2형(40) = 70점만으로 합격 가능**
- 환경: 클라우드 CBT (구름EDU), 자동완성 없음, 함수명 암기 필수

---

## 유형별 출제 내용

### 작업형 1형 — 데이터 전처리
- 결측치 처리, 이상값 제거
- 조건 필터링, groupby 집계, 정렬
- 스칼라 값 하나 print하는 형태

```python
import pandas as pd
df = pd.read_csv('data.csv')
# 예: 특정 조건 필터 후 값 추출
print(df[df['col'] > 0]['target'].mean())
```

### 작업형 2형 — ML 모델링 (40점 핵심)
정형화된 템플릿 구조 — 암기 가능

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. 데이터 로드
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# 2. 전처리
X = train.drop(['target', 'id'], axis=1)
y = train['target']
X_test = test.drop(['id'], axis=1)

# 3. 학습/검증 분리
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. 모델 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. 평가
pred = model.predict(X_val)
print(accuracy_score(y_val, pred))

# 6. 제출 파일 저장
result = model.predict(X_test)
pd.DataFrame({'id': test['id'], 'target': result}).to_csv('result.csv', index=False)
```

### 작업형 3형 — 가설검정 / 통계분석
소문항 3~4개 구성. 주요 검정:

```python
from scipy import stats

# 단일표본 t-검정
stats.ttest_1samp(df['col'], popmean=0)

# 독립표본 t-검정
stats.ttest_ind(group1, group2)

# 대응표본 t-검정
stats.ttest_rel(before, after)

# 카이제곱 독립성 검정
stats.chi2_contingency(pd.crosstab(df['A'], df['B']))

# 정규성 검정 (Shapiro-Wilk)
stats.shapiro(df['col'])

# 일원배치 ANOVA
stats.f_oneway(group1, group2, group3)
```

---

## 핵심 라이브러리

| 라이브러리 | 주요 용도 |
|---|---|
| `pandas` | 데이터 전처리 전반 (필수) |
| `numpy` | 수치 계산 |
| `sklearn` | 모델링, 전처리(StandardScaler, train_test_split) |
| `scipy.stats` | 가설검정 |
| `statsmodels` | 회귀분석, 로지스틱 회귀 |

---

## 준비 우선순위

```
1순위: 작업형 2형 템플릿 암기 (40점, 가장 ROI 높음)
2순위: 작업형 1형 pandas 숙달 (30점, groupby/필터/집계)
3순위: 작업형 3형 t-검정 + 카이제곱 (30점, 나머지는 시간 되면)
```

---

## 실전 팁

- **공식 체험 환경**: dataq.goorm.io — 시험 2~3일 전 반드시 접속해서 환경 적응
- 자동완성 없음 → 주요 함수명 손암기 필요
- `dir()`, `help()` 활용해서 패키지 탐색 가능
- 기출 풀이: datamanim.com

---

## 일정 (참고)

필기 합격 후 실기 응시 자격 생김. 필기 합격 발표 확인 후 실기 일정 등록.
