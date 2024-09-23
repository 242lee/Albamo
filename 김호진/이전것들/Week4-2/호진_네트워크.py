# 프로그래머스
# 네트워크

from collections import deque

def solution(n, computers):
    # 그룹의 개수 셀 거임
    answer = 0
    # bfs로 풀 거임
    dq = deque()
    # 컴퓨터 개수만큼 visited 생성
    v = [0] * n     # -> 각 컴퓨터가 몇 번 그룹에 속하는지 기록할 거임
    for i in range(n-1):
        # i번째 컴퓨터가 다른 컴퓨터랑 연결 됐는지 안 됐는지 구분할 거임
        flag = False
        for j in range(i+1, n):
            # i번 컴퓨터가 j번 컴퓨터랑 연결됐는지 확인
            if computers[i][j] == 1:
                # 연결됐다면 다시 확인하러 오지 않게 0으로 바꾸고
                computers[i][j] = 0
                # deque에 j번째 컴퓨터를 append
                # -> j번째 컴퓨터가 또 어떤 컴퓨터랑 연결됐는지 검사할 예정
                dq.append(j)
                flag = True
        # i번째 컴퓨터가 다른 컴퓨터랑 하나라도 연결됐으면 bfs 탐색 시작
        if flag == True:
            # 이번 bfs 탐색 그룹의 번호 부여
            answer += 1
            v[i] = answer
            while dq:
                x = dq.popleft()
                v[x] = answer
                # 이 순회는 위의 for j in range(i+1, n): 에서처럼 
                # 순차적으로 행을 탐색하는 것이 아닌,
                # dq에 의해 무작위 행을 순회하는 것이므로 
                # x+1부터 시작하지 않고 n개를 전부 순회해야 함
                # x+1부터 시작하면 누락되는 연결이 생김
                for y in range(n):
                    if computers[x][y] == 1:
                        computers[x][y] = 0
                        dq.append(y)
    for i in range(n):
        if v[i] == 0:
            answer += 1
            v[i] = answer

    return answer


# print(solution(1, [[1]]))
# print(solution(2, [[1, 0], [0, 1]]))
# print(solution(2, [[1, 1], [1, 1]]))
# print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
# print(solution(4, [[1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1]]))
print(solution(4, [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]))
