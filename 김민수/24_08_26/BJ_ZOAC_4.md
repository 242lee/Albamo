# 백준 ZOAC_4
### 문제 설명
W 개씩 H행
세로로 N칸 또는 가로로 M칸 이상 비우고 앉아야 함.
다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나 가로줄 번호의 차가
M보다 큰 곳에만 앉을 수 있다.

즉, 다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나
가로줄 번호의 차가 M보다 큰 곳에만 앉을 수 있다.

강의실이 수용할 수 있는 최대 인원 수를 출력한다.

### 첫 번쨰 풀이

```python
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
```
> 메모리 초과가 났다. -> 2차원 배열을 사용했기 때문

### 정답 코드
```python
H, W, N, M = map(int, input().split())

# (N+1) 칸마다 한 명을 배치할 수 있는 행의 수와 열의 수를 계산
row_count = (H + N) // (N + 1)
col_count = (W + M) // (M + 1)

# 최대 인원 수는 가능한 행 수와 열 수를 곱한 값
max_seat = row_count * col_count

print(max_seat)
```
1. 행의 수 계산 (row_count)
세로로 N+1 간격마다 학생을 배치한다고 가정해 봅시다. 강의실의 세로 길이는 H입니다. 세로로 학생을 배치할 수 있는 최대 행의 수(row_count)는 다음과 같이 계산할 수 있습니다:

row_count = (H + N) // (N + 1)
이 계산식은 N+1 간격으로 최대 몇 개의 행에 학생을 배치할 수 있는지를 의미합니다. 예를 들어:

H = 6, N = 1이면 (6 + 1) // (2) = 3입니다.
즉, 6행짜리 강의실에서는 2칸마다 한 명씩 학생을 배치할 수 있어, 총 3개의 행에 학생을 배치할 수 있습니다.

> 2차원 배열을 사용하지 않아도 되므로 메모리 사용량이 매우 적다!