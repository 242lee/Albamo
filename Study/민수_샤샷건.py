def find_nth_pressed_character(board, pressed_input, n):
    # board와 동일한 크기의 visited 배열을 0으로 초기화
    # 이 배열은 키보드 위치가 눌렸는지를 0(누르지 않음)과 1(누름)로 기록하는 역할을 함
    visited = [[0] * len(board[0]) for _ in range(len(board))]

    # 각 문자의 위치를 저장할 딕셔너리 생성
    # 키: 문자, 값: (행, 열) 위치의 튜플로 구성
    # 이를 통해 빠르게 눌린 문자의 좌표를 찾을 수 있음
    char_positions = {}
    for i, row in enumerate(board):  # i는 행 번호, row는 해당 행의 문자열
        for j, char in enumerate(row):  # j는 열 번호, char는 해당 위치의 문자
            char_positions[char] = (i, j)

    # 눌린 문자에 해당하는 위치를 visited 배열에 표시
    # pressed_input의 각 문자에 대해 그 문자가 위치한 좌표를 찾아서 1로 표시
    for char in pressed_input:
        if char in char_positions:  # board에 있는 문자인지 확인
            x, y = char_positions[char]  # 해당 문자의 좌표 (행, 열) 정보 가져옴
            visited[x][y] = 1  # 방문 표시 (눌린 위치를 1로 설정)

    # visited 배열에서 n번째 1이 있는 좌표 찾기
    # 왼쪽 위에서 오른쪽 아래로 순회하며, 눌린 순서대로 카운트하여 n번째 눌린 위치를 찾음
    count = 0
    target_position = None  # 찾는 위치의 좌표를 저장할 변수
    for i in range(len(visited)):  # 행을 순회
        for j in range(len(visited[i])):  # 열을 순회
            if visited[i][j] == 1:  # 눌린 위치(1)인 경우
                if count == n - 1:  # 0-based index이므로 n번째 눌린 위치는 n-1
                    target_position = (i, j)  # n번째 눌린 위치를 찾음
                    break  # 위치를 찾았으므로 내부 for문 탈출
                count += 1  # 눌린 위치(1)를 찾을 때마다 카운트 증가
        if target_position:  # 위치를 찾았으면 외부 for문도 탈출
            break

    # board에서 해당 좌표에 있는 문자 반환
    # target_position에 있는 문자를 찾아서 반환
    target_character = board[target_position[0]][target_position[1]]
    return target_character


# 입력받기
board = [input() for _ in range(4)]  # 키보드 배열을 4줄 입력받아 리스트 형태로 저장
pressed_input = input()  # 눌린 문자 리스트 입력받기

# 5번째 눌린 문자 찾기
target_character = find_nth_pressed_character(board, pressed_input, 5)
print(target_character)  # 5번째 눌린 문자 출력
