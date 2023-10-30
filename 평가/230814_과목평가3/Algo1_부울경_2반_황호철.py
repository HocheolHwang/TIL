def handmade_max(numbers):
    max_value = 0
    for number in numbers:
        if max_value < number:
            max_value = number
    return max_value


di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for i in range(N):
        for j in range(N):
            num_lst = []
            for k in range(5):
                if 0 <= i + di[k] < N and 0 <= j + dj[k] < N:
                    num_lst.append(MAP[i + di[k]][j + dj[k]])
            if handmade_max(num_lst) == MAP[i][j] and num_lst.count(handmade_max(num_lst)) == 1:
                cnt += 1

    print(f'#{tc} {cnt}')
