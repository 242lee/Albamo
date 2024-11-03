# 백준 32381 Coloring 2: Electric Boogaloo 골2
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
queries = list(map(int, input().split()))

row_flip_count = 0
col_flip_count = 0
row_flipped = set()
col_flipped = set()
result = []

current_black_cells = 0

for target_black_cells in queries:
    if current_black_cells == target_black_cells:
        result.append("No Flip")
        continue
    
    if row_flip_count % 2 == 0:
        row = len(row_flipped) + 1
        row_flipped.add(row)
        current_black_cells += N
        result.append(f"R {row}")
        row_flip_count += 1
    else:
        col = len(col_flipped) + 1
        col_flipped.add(col)
        current_black_cells += N
        result.append(f"C {col}")
        col_flip_count += 1

if current_black_cells != queries[-1]:
    print(-1)
else:
    print("\n".join(result))