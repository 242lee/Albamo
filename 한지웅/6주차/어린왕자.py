def checkInclude(coordX, coordY, radius):
    global includeStart, includeEnd

    betweenStartDouble = ((startX - coordX)**2 + (startY - coordY)**2)
    betweenEndDouble = ((endX - coordX)**2 + (endY - coordY) ** 2)
    boolIncludeStart = betweenStartDouble > radius**2
    boolIncludeEnd = betweenEndDouble > radius**2
    if boolIncludeEnd == True and boolIncludeStart == True:
        return
    elif boolIncludeEnd == True:
        includeEnd += 1
        return
    elif boolIncludeStart == True:
        includeStart += 1
        return
    else:
        return

T = int(input())
for tc in range(T):
    includeStart = 0
    includeEnd = 0
    startX, startY, endX, endY = map(int, input().split())
    numOfPlanet = int(input())
    for _ in range(numOfPlanet):
        coordX, coordY, radius = map(int,input().split())
        checkInclude(coordX, coordY, radius)
    print(includeStart+includeEnd)
