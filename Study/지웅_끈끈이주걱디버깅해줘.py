N, M = map(int,input().split())
Plants = []
for i in range(M):
    # C가 0이면 아래에서 올라옴. 1이면 위에서 내려옴
    # 끈끈이 주걱의 좌표 : Xi, Hi
    # 파리가 이동할 땐, 현 위치 보다 한칸 아래, 혹은 그 이상을 가야 한다.
    # 즉, 올라가는건 상관 없고, 내려가는게 문제임.
    C, Xi, Hi = map(int,input().split())
    Plants.append((C, Xi, Hi))

Plants.sort(key=lambda x: x[1])
# print(Plants)
# 시작 좌표를 정의한다. xIndex가 N에 정상도달한다면 탈출, 아니라면 실패.
xIndex = 0
yIndex = 0
plantIndex = 0

def flyTrip():
    global xIndex, yIndex, plantIndex
    if len(Plants) == 0:
        return 'stay'
    while plantIndex < M:
        # 다음 식물은?
        pivot = Plants[plantIndex]
        nextX = pivot[1]
        nextY = pivot[2]
        nextType = pivot[0]

        # case 1. 아래서 위로 올라오는 끈끈이 + 나의 현 좌표보다 같거나 높다.
        if nextType == 0 and nextY >= yIndex:
            xIndex = nextX
            yIndex = nextY + 1
        # case 2. 아래서 위로 올라오는 끈끈이, 나의 현 좌표보다 낮다.
        elif nextType == 0 and nextY < yIndex:
            # 내려가는 것엔 한계가 있음에 주의
            yIndex = yIndex - (nextX - xIndex)
            xIndex = nextX
        # case 3. 위에서 아래로 내려오는 끈끈이라면 일단 가본다.
        elif nextType == 1:
            # case 3-1. 이 때 y좌표가 끈끈이에 걸린다면 adios
            yIndex = yIndex - (nextX - xIndex)
            xIndex = nextX
            if yIndex >= nextY:
                return 'adios'
            # case 3-2. adios에 걸리지 않는다면 정상 진행한다.

        # 여기 까지 왔다는 것은 adios에 걸리지 않았다는 말.
        plantIndex += 1
    # while문을 통과했다면, N까지는 도달할 수 있다는 말임.
    # 여기서부터 N,0에 도달할 수 있는지 여부를 판단한다.
    if yIndex -1 * (N - xIndex) <= 0:
        return 'stay'
    else:
        return 'adios'

print(flyTrip())
