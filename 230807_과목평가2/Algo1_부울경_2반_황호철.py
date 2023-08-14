def handmade_max(numbers):  # 내장함수 'max'의 기능을 수행하는 함수 직접 제작
    max_num = 0
    for number in numbers:
        if max_num < number:
            max_num = number
    return max_num


def handmade_min(numbers):  # 내장함수 'min'의 기능을 수행하는 함수 직접 제작
    min_num = numbers[0]
    for number in numbers:
        if min_num > number:
            min_num = number
    return min_num


def handmade_abs(a, b):  # 내장함수 'abs'의 기능을 수행하는 함수 직접 제작
    abs_num = handmade_max([a, b]) - handmade_min([a, b])
    return abs_num


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    MAP = [list(map(int, input().split())) for _ in range(N)]

    new_lst = []  # 빈 리스트 생성
    for i in range(lst[0], lst[2] + 1):
        for j in range(lst[1], lst[3] + 1):
            new_lst.append(MAP[i][j])  # 빈 리스트에 평지로 만들 평탄화 영역의 숫자 추가

    total_num = 0
    for num in new_lst:
        total_num += num
    avg = total_num // len(new_lst)  # 평탄화 영역의 평균값 계산

    cnt = 0
    for num in new_lst:
        cnt += handmade_abs(num, avg)  # 각 영역을 평탄화 하기 위해 필요한 작업 수 계산

    print(f'#{tc} {cnt}')  # 형식에 맞게 출력
