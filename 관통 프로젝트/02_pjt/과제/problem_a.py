
import pandas as pd


# 데이터 파일 경로 설정
csv_file = 'data/NFLX.csv'


# 'Date', 'Open', 'High', 'Low', 'Close' 열만 사용하여 데이터프레임 생성
df = pd.read_csv(csv_file, usecols= ['Date', 'Open', 'High', 'Low', 'Close'])


# 데이터 읽어오기
print(df)