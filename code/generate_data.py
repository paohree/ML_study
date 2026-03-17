import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

나이 = np.random.randint(20, 65, n).astype(float)
연봉 = (나이 * 100000 + np.random.randint(-500000, 1000000, n)).astype(float)
방문횟수 = np.random.randint(1, 30, n).astype(float)
구매금액 = (방문횟수 * 3000 + np.random.randint(-5000, 20000, n)).astype(float)
성별 = np.random.choice(['남', '여'], n)
지역 = np.random.choice(['서울', '부산', '대구', '인천', '광주'], n)
등급 = np.random.choice(['낮음', '보통', '높음'], n, p=[0.4, 0.4, 0.2])
이탈여부 = ((방문횟수 < 5) | (구매금액 < 10000)).astype(int)

df = pd.DataFrame({
    '나이': 나이,
    '연봉': 연봉,
    '구매금액': 구매금액,
    '방문횟수': 방문횟수,
    '성별': 성별,
    '지역': 지역,
    '등급': 등급,
    '이탈여부': 이탈여부
})

# 이상치 삽입
df.loc[10, '나이'] = 999
df.loc[25, '나이'] = 1
df.loc[50, '연봉'] = 999999999
df.loc[75, '구매금액'] = -99999

# 결측치 삽입 (랜덤하게 약 5%)
for col in ['나이', '연봉', '구매금액', '방문횟수', '지역']:
    idx = np.random.choice(n, int(n * 0.05), replace=False)
    df.loc[idx, col] = np.nan

df.to_csv('customers.csv', index=False)
print(f"생성 완료: {len(df)}행")
print(df.isnull().sum())
print(df.describe())
