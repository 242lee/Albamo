# 1, 2, 3 의 방식을 dfs로 진행한다
# 그렇다면 시간 초과 발생 가능성 높음.
    # 그렇다면 ? DP ?
    # 뭐야 통과네

def func_triple(numb):
    if numb % 3 == 0:
        return numb // 3
    else:
        return False

def func_double(numb):
    if numb % 2 == 0:
        return numb // 2
    else:
        return False

def dfs(numb, lst, cnt):
    global mx_lst, mx
    if cnt > mx:
        return
    if numb == 1:
        if mx > cnt:
            mx = cnt
            mx_lst = lst
        return
    trip = func_triple(numb)
    doub = func_double(numb)
    if trip != False:
        dfs(trip, lst + [trip], cnt + 1)
    if doub != False:
        dfs(doub, lst + [doub], cnt + 1)
    dfs(numb - 1, lst + [numb - 1], cnt + 1)

mx = 9876543212
mx_lst = None
start_number = int(input())
dfs(start_number, [start_number], 0)
print(mx)
for _ in mx_lst:
    print(_, end=' ')
