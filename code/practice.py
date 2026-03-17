import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# =====================
# 1. 데이터 불러오기
# =====================
df = pd.read_csv('customers.csv')

print("=== 원본 데이터 (앞 5행) ===")
print(df.head())
print(f"\n총 {len(df)}행, {len(df.columns)}개 컬럼")

# =====================
# 2. 결측치 확인
# =====================
print("\n=== 결측치 확인 ===")
print(df.isnull().sum())

# =====================
# 3. 이상치 확인
# =====================
print("\n=== 기본 통계 (이상치 힌트) ===")
print(df[['나이', '연봉', '구매금액', '방문횟수']].describe())

# =====================
# 4. 이상치 처리 (말이 안 되는 값 → NaN으로)
# =====================
df.loc[df['나이'] > 100, '나이'] = np.nan
df.loc[df['나이'] < 10, '나이'] = np.nan
df.loc[df['구매금액'] < 0, '구매금액'] = np.nan

print("\n=== 이상치 제거 후 결측치 ===")
print(df.isnull().sum())

# =====================
# 5. 결측치 처리 (중앙값으로 채우기)
# =====================
df['나이'] = df['나이'].fillna(df['나이'].median())
df['연봉'] = df['연봉'].fillna(df['연봉'].median())
df['구매금액'] = df['구매금액'].fillna(df['구매금액'].median())
df['방문횟수'] = df['방문횟수'].fillna(df['방문횟수'].median())
df['지역'] = df['지역'].fillna('기타')

print("\n=== 결측치 처리 후 ===")
print(df.isnull().sum())

# =====================
# 6. 인코딩
# =====================
# Ordinal: 등급 (낮음 < 보통 < 높음 순서 있음)
등급_순서 = {'낮음': 0, '보통': 1, '높음': 2}
df['등급'] = df['등급'].map(등급_순서)

# One-Hot: 성별, 지역 (순서 없음)
df = pd.get_dummies(df, columns=['성별', '지역'])

# =====================
# 7. 표준화
# =====================
scaler = StandardScaler()
df[['나이', '연봉', '구매금액', '방문횟수']] = scaler.fit_transform(
    df[['나이', '연봉', '구매금액', '방문횟수']]
)

print("\n=== 최종 데이터 (앞 5행) ===")
print(df.head())
print(f"\n최종 컬럼: {list(df.columns)}")
