"""
W 개씩 H행
세로로 N칸 또는 가로로 M칸 이상 비우고 앉아야 함.
다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나 가로줄 번호의 차가
M보다 큰 곳에만 앉을 수 있다.

즉, 다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나
가로줄 번호의 차가 M보다 큰 곳에만 앉을 수 있다.

강의실이 수용할 수 있는 최대 인원 수를 출력한다.
"""
H, W, N, M = map(int, input().split())
seat = [[0] * W for _ in range(H)]
max_seat = 0
seat[0][0] = 1
print(seat)
for i in range(H):
    for j in range(W):
        if seat[i][j] == 1 and i+N+1 < H and j+M+1 < W:
            seat[i][j+M+1] = 1
            seat[i+N+1][j] = 1
            seat[i+N+1][j+M+1] = 1

for p in range(H):
    for q in range(W):
        if seat[p][q] == 1:
            max_seat += 1

print(max_seat)