def Max_Point(row=0, col=0):
    # 모든 행(row)을 다 선택 했을 경우 0을 반환
    if row == N:
        return 0

    # Memoization 안에 이미 계산된 값이 있으면 해당 값을 반환 (중복 계산 회피)
    if DP[col] != -1:
        return DP[col]

    # 최대값 0으로 초기화
    max_point = 0

    # N 길이의 열(col)을 순회
    for i in range(N):

        # 역순으로 i번째 열을 선택하지 않았을 경우에 계산 진행
        if not col & (1 << i):

            # 해당 행과 열의 과녁 점수를 먼저 더함
            # 이후 행의 인덱스를 1 더하고, 선택된 열은 비트마스킹으로 선택했음을 기록
            point = S[row][i] + Max_Point(row + 1, col | (1 << i))
            max_point = max(max_point, point)

    # Memoization 안에 이번 열에 대한 최대 값 저장
    DP[col] = max_point
    return DP[col]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    # 점수를 저장할 Memoization 초기화
    DP = [-1] * (1 << N)

    # 결과값에 함수의 반환 값을 저장하고 출력
    result = Max_Point()
    print(f'#{tc} {result}')
