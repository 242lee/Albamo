# 백준 2292번 벌집 브2

n = int(input())

b = 1
i = 1

while b < n:
    b += 6 * i
    i += 1

print(i)