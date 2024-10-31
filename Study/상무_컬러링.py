# x개의 열이 뒤집혀져 있는 경우에, 안 뒤집힌 행 안에는 x개의 검은색 칸과 n-x개의 흰색 칸이 있다.
# 이것을 뒤집으면 검은색 칸의 개수는 n-x개가 되고, 바꿔 말하면 검은색 칸의 개수가 n-2x 개만큼 늘어난다.
# 반대로 뒤집힌 행을 되돌릴 때는 검은색 칸의 개수가 n-2x 개만큼 줄어든다. 
# 행과 열을 반대로 생각해도 마찬가지이다.

# N = 정사각형 한 변, 홀수
# Q = 횟수
N, Q = [int(x) for x in input().split()]
black_counts = [int(x) for x in input().split()]

# 행과 열의 뒤집힌 값 초기화
flipped_col_count = flipped_row_count = 0
# 검은색 칸 개수 초기화
black_count_current = 0
answer = []
for black_count in black_counts:
    # 이전 시행에서 채울 검은 칸 개수
    black_count_previous = black_count_current
    # 현재 내가 채울 검은 칸 개수
    black_count_current = black_count
    # 현재 내가 채울 검은 칸에서 이전 시행에서 채울 검은 칸을 뺀 값
    # 즉, 내가 뒤집어야할 흰색 칸의 개수
    white_to_flip = black_count_current - black_count_previous
    # 뒤집어야할 흰색 칸의 개수가 
    if white_to_flip == N - (flipped_col_count * 2) and flipped_row_count < N:
        answer.append(f'R {flipped_row_count + 1}')
        flipped_row_count += 1
    elif white_to_flip == -(N - (flipped_col_count * 2)) and flipped_row_count > 0:
        answer.append(f'R {flipped_row_count}')
        flipped_row_count -= 1
    elif white_to_flip == N - (flipped_row_count * 2) and flipped_col_count < N:
        answer.append(f'C {flipped_col_count + 1}')
        flipped_col_count += 1
    elif white_to_flip == -(N - (flipped_row_count * 2)) and flipped_col_count > 0:
        answer.append(f'C {flipped_col_count}')
        flipped_col_count -= 1
    else:
        print('-1')
        break
else:
    print('\n'.join(answer))