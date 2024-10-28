minN, maxN = map(int, input().split())
is_square_free = [True] * (maxN - minN + 1)

# 2부터 maxN의 제곱근까지의 수를 순회
for i in range(2, int(maxN**0.5) + 1):
    square = i * i 

    start = (minN + square - 1) // square * square
    
    for j in range(start, maxN + 1, square):
        is_square_free[j - minN] = False

# True로 남아있는 값들의 개수 카운트
result = sum(is_square_free)
print(result)
