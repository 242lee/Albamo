# 잘못된 숫자를 말할 때마다 0을 외쳐서 가장 최근에 쓴 수 지우기

K = int(input())
stack = []
for _ in range(K):
    a = int(input())
    if a == 0 and stack:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))

