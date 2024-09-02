'''
적어도 M미터의 나무 필요
절단기의 설정 높이보다 높은 나무 모두 절단
절단기 설정 높이의 최댓값

이진 탐색 사용
근데 제대로 이해못함
대충은 한듯
그림으로 설명할 이상무 구함
'''
# n = 나무의 수 
# m = 가져가려고 하는 나무의 길이
n, m = map(int, input().split())

# 나무의 길이
trees = list(map(int, input().split()))

start = 0
end = max(trees)

result = 0
while (start <= end):
    # 가져가게 될 나무의 길이
    sum = 0 
    # 절단기의 높이
    mid = (start + end) // 2 
    for i in trees:
        # 절단기보다 나무의 길이가 길면 자른 나머지를 sum에 추가
        if i > mid: 
            sum += i - mid
    # 이진탐색
    # 가져가야하는 길이보다 sum이 작으면
    # mid의 왼쪽 부분 탐색
    if sum < m:
        end = mid - 1
    
    # 가져가야하는 길이보다 크거나 같으면
    else:
        result = mid
        # mid의 오른쪽 부분 탐색
        start = mid + 1

print(result)