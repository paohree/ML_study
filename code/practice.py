import pandas as pd
import numpy as np

# 샘플 데이터 만들기
data = {
    '나이': [25, 30, None, 45, 60],
    '구매금액': [30000, 50000, 20000, None, 80000],
    '방문횟수': [10, 5, 3, 8, 1],
    '지역': ['서울', '부산', '서울', '대구', '부산'],
    '이탈여부': [0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

print("=== 원본 데이터 ===")
print(df)
print()

print("=== 결측치 확인 ===")
print(df.isnull().sum())
print()

print("=== 결측치를 평균으로 채우기 ===")
df['나이'] = df['나이'].fillna(df['나이'].mean())
df['구매금액'] = df['구매금액'].fillna(df['구매금액'].mean())
print(df)
print()

print("=== 원핫 인코딩 (지역) ===")
df = pd.get_dummies(df, columns=['지역'])
print(df)
