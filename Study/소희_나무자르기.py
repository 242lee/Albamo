# N: 나무의 개수, M: 필요한 나무의 길이
N, M = map(int, input().split())

# 나무의 높이
trees = list(map(int, input().split()))

# 이진 탐색 : 시작점(start)과 끝점(end) 설정
# 절단기의 시작 높이는 1, 최대 높이는 모든 나무의 높이의 합(sum(trees))으로 설정
start, end = 1, sum(trees)

while start <= end:
    # 중간 값(mid)을 현재 절단기의 높이로 설정
    mid = (start + end) // 2
    
    # 현재 높이(mid)에서 나무를 자를 때 얻는 나무의 총 길이(cut)
    cut = 0

    # 각 나무의 높이를 확인하여, 나무가 절단기의 높이보다 높은 경우 자르고, 자른 길이만큼 cut에 더함
    for tree in trees:
        if tree > mid:
            cut += tree - mid

    # 자른 나무의 길이가 필요한 길이(M) 이상인 경우
    if cut >= M:
        # 더 높은 높이에서 자를 수 있는지 확인하기 위해 절단기 높이를 올려봄
        start = mid + 1
    else:
        # 자른 나무의 길이가 필요한 길이(M)보다 적은 경우
        # 절단기의 높이를 낮추어 더 많이 자를 수 있도록 함
        end = mid - 1

# 이진 탐색이 종료되면 end가 최대 절단기 높이가 됨
print(end)
