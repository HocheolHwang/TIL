
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


# 'Date' 열을 월로 추출하여 그룹화하고 평균 종가 계산
monthly_avg_close = df_after_2021.groupby(df_after_2021['Date'].dt.to_period('M')).mean()


# 그래프에 제목과 축 레이블 추가
plt.plot(monthly_avg_close['Date'], monthly_avg_close['Close'])


# 그래프에 제목과 축 레이블 추가
plt.title('Monthly NFLX Close Price')
plt.xlabel('Date')
plt.ylabel('Average Close Price')


# x 축 레이블 회전시키기
plt.xticks(rotation=45)


# 그래프 표시
plt.show()
