# 제곱수이다.
# 각 제곱수는 2*n - 1 개가 최소 개수이다.
# 제곱수 사이의 수의 규칙 ?
# f(n^2) = 2*n - 1
# sqrt(n)을 해보면 정수일 때와 실수일 때로 나눈다.
# (정수 부분을 따로 빼서 2*n - 1을 해준 값을 변수로 따로 빼서 지정한다.)
# 실수일 때면, 그 실수를 내림한 수에서 0.5를 더한 후 둘이 뺀다.
# 뺀 값이 음수면 따로 뺀 변수에서 1을 더해주고 양수면 2를 더해준다.
import math

def min_space_moves(x, y):
    distance = y - x
    n = int(math.sqrt(distance))
    
    if n * n == distance:
        return 2 * n - 1
    elif n * n < distance <= n * n + n:
        return 2 * n
    else:
        return 2 * n + 1

# Input and Output
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(min_space_moves(x, y))
