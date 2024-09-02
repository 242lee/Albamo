# 나무 자르기

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, sum(trees)

while start <= end:
    mid = (start + end) // 2
    cut = 0

    for tree in trees:
        if tree > mid:
            cut += tree - mid

    if cut >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)