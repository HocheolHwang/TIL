def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while True:
        middle = (start + end) // 2
        if a[middle] == key:
            return True  # 검색 성공
        elif a[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
        if key < a[start] or key > a[end]:
            return False  # 검색 실패

lst = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(lst, 7, 7))