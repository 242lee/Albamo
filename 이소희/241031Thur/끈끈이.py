import sys
input = sys.stdin.readline

# 출구위치 N, 끈끈이 수 M
N, M = map(int, input().split())

if M == 0:
    print('stay')
else:
    kke = [list(map(int, input().split())) for _ in range(M)]
    kke.sort(key=lambda x: x[1])    # x 좌표 기준으로 정렬하여 순차적으로 확인

    pre_i, pre_j = 0, 0             # 초기 위치 설정

    for dir, i, j in kke:
        if dir == 0:                # 아래에서 올라오는 끈끈이주걱
            pre_j = max(j + 1, pre_j - (i - pre_i))
        elif dir == 1:              # 위에서 내려오는 끈끈이주걱
            if j - 1 < pre_j - (i - pre_i):
                print('adios')
                break
            pre_j = pre_j - (i - pre_i)
        pre_i = i
    else:
        if 0 < pre_j - (N - pre_i):
            print('adios')
        else:
            print('stay')
