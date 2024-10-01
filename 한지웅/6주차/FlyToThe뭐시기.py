# dfs하면 시간초과 메모리초과 overflow등의 문제 발생 => dp?
# end - start
# 1 : 1
# 2 : 1 1
# 3 : 1 1 1
# 4 : 1 2 1
# 5 : 1 2 1 1 or 1 1 2 1
# 6 : 1 2 2 1 ...

# 4번부터 다음의 규칙으로 진행 (양쪽 1 빼고)
# 2
# (2 1) (2 2)
# (2 2 1) (2 2 2) (2 3 2)
# (2 2 2 2) (2 3 2 2) (2 3 3 2)
# (2 2 3 2 2) (2 3 3 2 2) (2 3 3 3 2) (2 3 4 3 2)
# 주어진 숫자에 맞게 해당 연산을 진행하면 되겠구나 !
#                 1 : 1 : 0 + 1
#                1 1 : 2 : 1 + 1
#               1 2 1 : 4 : 2 + 2
#              1 2 2 1 : 6 : 4 + 2
#             1 2 3 2 1 : 9 : 6 + 3
#            1 2 3 3 2 1 : 12 : 9 + 3
#           1 2 3 4 3 2 1 : 16 : 12 + 4
#          1 2 3 4 4 3 2 1 : 20 : 16 + 4
#         1 2 3 4 5 4 3 2 1 : 25 : 20 + 5

def distanceCalculator(numb):
    res = 2
    currentNumb = 2
    AddNumb = 2
    AddCnt = 0
    while True:
        currentNumb = currentNumb + AddNumb
        AddCnt += 1
        res += 1
        # print('numb', numb)
        if currentNumb >= numb:
            # print('res',res,'currentNumb',currentNumb)
            return res
        if AddCnt == 2:
            AddNumb += 1
            AddCnt = 0
    return

def Funnel(numb):
    if numb == 1:
        return 1
    elif numb == 2:
        return 2
    elif numb == 3:
        return 3
    else:
        res = distanceCalculator(numb)
        return res


TC = int(input())
for _ in range(TC):
    start, end = map(int, input().split())
    ans = Funnel(end - start)
    print(ans)
