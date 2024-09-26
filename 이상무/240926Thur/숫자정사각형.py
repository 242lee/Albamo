# N x M
# N과 M의 숫자 비교
# 둘 중 작은수를 비교해서 작은 정사각형을 만든다.
# N이 더 작다고 가정하자.
# 작은 정사각형을 토대로 (0, 0)부터 정사각형을 만들 수 있는 영역까지 만듬
# 만드는 방법은 (0, 0)에서 오른쪽으로 N - 1칸 아래쪽으로 N - 1칸 오른쪽, 아래쪽으로 N - 1 칸 이동해서 set에 넣은 길이가 1이면 


N, M = map(int,input().split())
square_box = [[] for _ in range(N)]

for i in range(N):
    square_box[i] = list(map(int,input()))

ans = []

# 사이즈가 큰 것을 판별한다.
if N >= M:
    size = M
else:
    size = N

i = 0
j = 0

while size > 0:
    # 시작점을 기준으로 사각형의 꼭짓점에 해당하는 부분이 일치하는지 확인한다.
    if square_box[i][j] == square_box[i+size-1][j] == square_box[i][j+size-1] == square_box[i+size-1][j+size-1]:
        # 일치한다면 사이즈의 제곱을 해준다.
        ans.append(size**2)
        break
    # 정사각형의 네 꼭짓점이 일치하지 않으면 오른쪽으로 한 칸 이동한다.
    j += 1
    
    # 이동했을 때 오른쪽 꼭짓점이 벗어나면 시작점을 기준으로 한 칸 아래로 간다.
    if j+size-1 >= M:
        j = 0
        i += 1
        
    # 이동했을 때 아래 꼭짓점이 벗어나면 시작점으로 가고 사이즈를 하나 줄여서 다시 실행한다.
    if i+size-1 >= N:
        size -= 1
        i = 0
        j = 0
        
print(max(ans))