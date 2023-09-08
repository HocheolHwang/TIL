
import pandas as pd
import matplotlib.pyplot as plt


# 데이터 파일 경로 설정
csv_file = 'data/NFLX.csv'


# 'Date', 'Open', 'High', 'Low', 'Close' 열만 사용하여 데이터프레임 생성
df = pd.read_csv(csv_file, usecols= ['Date', 'Open', 'High', 'Low', 'Close'])


# 'Date' 열을 datetime 형식으로 변환
df['Date'] = pd.to_datetime(df['Date'])


# 2021년 이후의 데이터 필터링
df_after_2021 = df[df['Date'] >= '2021-01-01']


# 최고 및 최저 종가 가져오기
max_price = df_after_2021['Close'].max()
min_price = df_after_2021['Close'].min()


# 최고 및 최저 종가 출력
print('최고 종가:', max_price)
print('최저 종가:', min_price)
