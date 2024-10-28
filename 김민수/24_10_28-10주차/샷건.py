def find_nth_pressed_character(board, pressed_input, n):
    # board와 동일한 크기의 visited 배열을 0으로 초기화
    visited = [[0] * len(board[0]) for _ in range(len(board))]

    # 각 문자의 위치를 저장할 딕셔너리 생성
    char_positions = {}
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            char_positions[char] = (i, j)

    # 눌린 문자에 해당하는 위치를 visited 배열에 표시
    for char in pressed_input:
        if char in char_positions:
            x, y = char_positions[char]
            visited[x][y] = 1

    # visited 배열에서 n번째 1이 있는 좌표 찾기
    count = 0
    target_position = None
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j] == 1:
                if count == n - 1:  # 0-based index이므로 n-1
                    target_position = (i, j)
                    break
                count += 1
        if target_position:
            break

    # board에서 해당 좌표에 있는 문자 반환
    target_character = board[target_position[0]][target_position[1]]
    return target_character


# 입력받기
board = [input() for _ in range(4)]  # 키보드 배열 4줄 입력
pressed_input = input()  # 눌린 문자 입력

# 5번째 눌린 문자 찾기
target_character = find_nth_pressed_character(board, pressed_input, 5)
print(target_character)
