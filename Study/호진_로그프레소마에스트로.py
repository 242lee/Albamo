# 백준 31937 로그프레소 마에스트로 실2

import sys
input = sys.stdin.readline

# 컴퓨터 개수 N(2~1000), 로그 개수 M(1~10000), 감염된 컴퓨터 개수 K(1~N)
N, M, K = map(int, input().split())
# 격리 시점에 감염 돼있던 컴퓨터들
infected = list(map(int, input().split()))

# 격리 시점에 감염된 컴퓨터가 한 개라면 그 컴퓨터가 최초 감염 컴퓨터
if K == 1:
    for _ in range(M): input()
    print(infected[0])
    exit()

# 시간 순서대로 정렬하기 위해 최소힙 사용
# (t가 중복이 없으므로 시간 순으로 정렬 가능)
logs = [list(map(int, input().split())) for _ in range(M)]
logs.sort()

# 최초 감염 컴퓨터 완전 탐색
for i in range(K):
    # N개의 컴퓨터 초기화
    computer = [0] * (N+1)
    # 첫 감염 컴퓨터를 infected[i]번째 컴퓨터로 가정
    computer[infected[i]] = 1

    # 감염된 컴퓨터 수 체크
    cnt = 1
    # (cnt = K가 되면 전부 감염시킨 것이므로
    # infected[i]번째 컴퓨터가 최초 감염 컴퓨터)

    # logs(전송 로그) 순회
    for t, a, b in logs:

        # 전송하는 컴퓨터가 감염돼있으면 
        # and 전송받는 컴퓨터가 첫 감염이면
        # > 전송받는 컴퓨터 감염시키기
        if computer[a] == 1 and computer[b] == 0:

            # 전송받는 컴퓨터가 감염되면 안 되는 컴퓨터면
            if b not in infected:
                # infected[i]번째 컴퓨터는 최초 감염 컴퓨터가 될 수 없다.
                break

            # 전송받은 컴퓨터 감염시키고
            computer[b] = 1
            # 감염된 컴퓨터 수 += 1
            cnt += 1
    
    # 감염시켜도 되는 컴퓨터만 감염시켰을 경우
    else:
        # 전부 감염됐으면
        if cnt == K:
            # infected[i]번째 컴퓨터가 최초 감염 컴퓨터
            print(infected[i])
            exit()

'''
로그 정렬을 힙큐로 로그 한 줄씩 힙 푸시를 했는데, 
인덱스 순회를 할 때 힙은 트리구조여서 
리스트의 sort처럼 인덱스 순으로 정렬되지 않아서 틀림
'''