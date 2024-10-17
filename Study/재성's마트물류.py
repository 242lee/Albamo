import sys
from collections import deque

# 파일 입력 설정 (제출 시 주석 처리 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def solve(N, K, line):
    robots = deque()
    parts = deque()
    
    # 로봇과 부품의 위치를 각각의 큐에 저장
    # enumerate를 사용하여 인덱스(위치)와 값을 동시에 처리
    for i, item in enumerate(line):
        if item == 'P':
            robots.append(i)
        elif item == 'H':
            parts.append(i)
    
    count = 0
    # 로봇과 부품이 모두 남아있는 동안 반복
    while robots and parts:
        robot = robots[0]  # 현재 처리할 로봇의 위치
        part = parts[0]    # 현재 처리할 부품의 위치
        
        # 로봇과 부품 사이의 거리가 K 이하인 경우 (매칭 성공)
        if abs(robot - part) <= K:
            count += 1              # 매칭 수 증가
            robots.popleft()        # 매칭된 로봇 제거
            parts.popleft()         # 매칭된 부품 제거
        # 부품이 로봇보다 왼쪽에 있는 경우 (현재 로봇으로 매칭 불가능)
        elif part < robot:
            parts.popleft()         # 해당 부품 제거 (더 이상 사용 불가)
        # 로봇이 부품보다 왼쪽에 있는 경우 (현재 부품으로 매칭 불가능)
        else:
            robots.popleft()        # 해당 로봇 제거 (더 이상 사용 불가)
    
    return count  # 총 매칭된 로봇-부품 쌍의 수 반환

# 입력 처리
N, K = map(int, input().split())
line = input().strip()

# 결과 출력
print(solve(N, K, line))
