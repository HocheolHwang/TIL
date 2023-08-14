def chl(lst, n, total, cnt):
    '''
    튕기는 거리마다 점수를 계산하여 더하고,
    튕기는 거리를 증가시켜 자기 자신을 다시 호출하는 재귀함수.
    튕기는 거리가 전체 리스트의 길이 'n'을 넘어 갈 경우,
    지금까지 더한 점수인 'total'을 반환한다.
    '''
    if cnt > n:
        return total if total > 0 else 0  # 범위를 벗어나면 'total'을 최종 반환. 점수가 0 이하면 0 반환
    i = 0
    for _ in range(n):  # 기본적으로 n번 반복
        if i > n - 1:  # 현재 튕기는 위치인 i가 리스트를 벗어날 경우 반복문 탈출
            break
        total += lst[i]  # 현재 튕긴 위치의 점수를 'total'에 합산
        i += cnt  # 다음 튕길 위치를 'cnt'만큼 증가시킴

    cnt += 1  # 튕기는 거리 증가
    return chl(lst, n, total, cnt)  # 튕기는 거리를 1 증가시킨 뒤에 다시 자기 자신을 호출


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bounce = list(map(int, input().split()))
    result = chl(bounce, N, 0, 1)  # total = 0, cnt = 1으로 첫 재귀함수 호출
    print(f'#{tc} {result}')
