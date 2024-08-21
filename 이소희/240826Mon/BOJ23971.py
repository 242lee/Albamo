# 세로 크기, 가로 크기, 세로줄 차, 가로줄 차
H, W, N, M = map(int, input().split())

rowCnt = (H + N) // (N + 1) # 행
colCnt = (W + M) // (M + 1) # 열

# 총 배치 가능한 사람의 수
maxCnt = rowCnt * colCnt

print(maxCnt)