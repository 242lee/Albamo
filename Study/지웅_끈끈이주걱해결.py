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
Plants.append((1,N,1))
# print(Plants)
# 시작 좌표를 정의한다. xIndex가 N에 정상도달한다면 탈출, 아니라면 실패.
xIndex = 0
yIndex = 0
plantIndex = 0

def flyTrip():
    global xIndex, yIndex, plantIndex
    if len(Plants) == 0:
        return 'stay'
    while plantIndex < len(Plants):
        # 다음 식물은?
        pivot = Plants[plantIndex]
        nextX = pivot[1]
        nextY = pivot[2]
        nextType = pivot[0]

        # 1. 일단 고
        yIndex = yIndex - (nextX - xIndex)
        xIndex = nextX

        # 2. yIndex 정리
        # case 1. 올라오는 끈끈이
        if nextType == 0:
            if yIndex <= nextY:
                yIndex = nextY + 1
        # case 2. 내려오는 끈끈이
        elif nextType == 1:
            if yIndex >= nextY:
                return 'adios'
        plantIndex += 1
    return 'stay'



print(flyTrip())
