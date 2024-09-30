import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

'''
비트 연산 : 비트 밀기에서는 앞뒤가 다름에 주의 (오른쪽부터 센다)

1 : 해당 자릿수 비트 OR
i번째 기차에(1 ≤ i ≤ N) x번째 좌석에(1 ≤ x ≤ 20) 사람을 태워라.
이미 사람이 타있다면 , 아무런 행동을 하지 않는다.

2 : 해당 자릿수만 0으로 만들고 비트 AND
i번째 기차에 x번째 좌석에 앉은 사람은 하차한다.
만약 아무도 그자리에 앉아있지 않았다면, 아무런 행동을 하지 않는다.

3 : 비트 왼쪽 밀기 (맨 왼쪽 처리필요)
i번째 기차에 앉아있는 승객들이 모두 한칸씩 뒤로간다.

4 : 비트 오른쪽 밀기 (자동 탈락됨)
i번째 기차에 앉아있는 승객들이 모두 한칸씩 앞으로간다.

'''

N, M = map(int, input().split())
trains = [0] * N  # 기차 상태를 저장할 리스트

for _ in range(M):
    command = list(map(int, input().split()))

    if command[0] == 1:  # 사람 태우기
        trains[command[1] - 1] |= (1 << (command[2] - 1))

    elif command[0] == 2:  # 사람 내리기
        trains[command[1] - 1] &= ~(1 << (command[2] - 1))

    elif command[0] == 3:  # 한 칸씩 뒤로 이동
        trains[command[1] - 1] = (trains[command[1] - 1] << 1) & ((1 << 20) - 1)

    elif command[0] == 4:  # 한 칸씩 앞으로 이동
        trains[command[1] - 1] = (trains[command[1] - 1] >> 1)

# 중복되지 않은 기차 상태 저장을 위한 set
visited = set(trains)

print(len(visited))