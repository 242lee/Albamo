# softeer

def max_robots_can_grab_parts(n, k, line):
    robots = []
    parts = []
    
    # 로봇과 부품의 위치를 저장
    for i in range(n):
        if line[i] == 'P':
            robots.append(i)
        elif line[i] == 'H':
            parts.append(i)
    
    count = 0
    part_used = [False] * len(parts)  # 부품 사용 여부 체크

    # 각 로봇에 대해 가장 먼 부품을 먼저 잡도록 처리
    for robot in robots:
        for i in range(len(parts)):
            if abs(robot - parts[i]) <= k and not part_used[i]:  # 거리 내에 있는지, 사용된 적 없는 부품인지 체크
                count += 1
                part_used[i] = True  # 부품 사용 처리
                break  # 해당 로봇은 부품을 잡았으므로 다음 로봇으로 이동
    
    return count

# 입력
n, k = map(int, input().split())
line = input()

# 결과 출력
print(max_robots_can_grab_parts(n, k, line))
