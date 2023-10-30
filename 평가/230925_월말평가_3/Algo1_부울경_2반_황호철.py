# 각 자리의 16진수에 해당하는 4자리 2진수를 연결시켜 놓은 딕셔너리
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = input()
    K = hex_to_bin[input()]  # Key 값은 받는 동시에 4자리 2진수로 전환한다.

    # 암호화된 16진수 P의 각 자리수를 4자리 2진수로 변환하여 리스트에 담는다.
    P_lst = []
    for p in P:
        P_lst.append(hex_to_bin[p])

    # 암호화 전 16진수의 각 자리수를 담을 리스트를 초기화한다.
    H_lst = []

    # 암호를 만드는 과정을 역산한다.
    # 원래 수 H의 각 자리수를 4자리 2진수로 표현한 값을 리스트에 담는다.
    for Pi in P_lst:
        H = ''
        for i in range(4):
            if K[i] == '1':
                H += '1' if Pi[i] == '0' else '0'
            else:
                H += '0' if Pi[i] == '0' else '1'
        H_lst.append(H)

    # 각 4자리 2진수에 해당하는 16진수 숫자를 문자열로 결과값에 추가한다.
    result = ''
    for Hi in H_lst:
        for key, value in hex_to_bin.items():
            if Hi == value:
                result += key

    print(f'#{tc} {result}')
