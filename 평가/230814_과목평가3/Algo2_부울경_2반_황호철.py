a = ['(', ')', '{', '}']


T = int(input())
for tc in range(1, T + 1):
    string = input()

    result = 0
    total = 0
    cnt = 0
    stack = []
    num_stack = []

    if string[0] not in a or string[-1] not in a:
        result = -1
    else:
        for s in string:
            if s in a:
                if not stack:
                    stack.append(s)
                else:
                    if stack[-1] == '(' and s == ')':
                        stack.pop()
                        for i in range(cnt):
                            total += int(num_stack.pop())
                        cnt = 0
                    elif stack[-1] == '{' and s == '}':
                        stack.pop()
                        if total == 0:
                            total = 1
                        for i in range(cnt):
                            total *= int(num_stack.pop())
                        cnt = 0
                    else:
                        stack.append(s)
                        cnt = 0

            else:
                cnt += 1
                num_stack.append(s)

        if string[0] == '(':
            total += int(num_stack[0])
        else:
            total *= int(num_stack[0])

    if stack:
        result = -1

    print(f'#{tc}', end=' ')
    print(f'{result}') if result == -1 else print(f'{total}')
