N = int(input())
stack = []
answer = []
flag = False

now = 1
for _ in range(N):
    num = int(input())

    while now <= num:
        stack.append(now)
        answer.append('+')
        now += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = True
        print('NO')
        break

if not flag:
    print('\n'.join(answer))