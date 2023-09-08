
import pandas as pd
import matplotlib.pyplot as plt


# 데이터 파일 경로 설정
csv_file = 'data/NFLX.csv'


# 'Date', 'Open', 'High', 'Low', 'Close' 열만 사용하여 데이터프레임 생성
df = pd.read_csv(csv_file, usecols= ['Date', 'Open', 'High', 'Low', 'Close'])


# 'Date' 열을 datetime 형식으로 변환
df['Date'] = pd.to_datetime(df['Date'])


# 2022년 이후의 데이터 필터링
df_after_2022 = df[df['Date'] >= '2022-01-01']


# 'Date'를 x 축으로, 각각 'High', 'Low', 'Close'를 y 축으로 하는 그래프 그리기
plt.plot(df_after_2022['Date'], df_after_2022['High'], label = 'High')
plt.plot(df_after_2022['Date'], df_after_2022['Low'], label = 'Low')
plt.plot(df_after_2022['Date'], df_after_2022['Close'], label = 'Close')


# 그래프에 제목과 축 레이블 추가
plt.title('High, Low, and Close Prices since January 2022')
plt.xlabel('Date')
plt.ylabel('Close Price')


# 범례 추가
plt.legend()


# x 축 레이블 회전시키기
plt.xticks(rotation=45)


# 그래프 표시
plt.show()
