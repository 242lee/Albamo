# a, b가 주어지면 , b까지의 1의 개수 합 - a까지의 1의 개수 합으로 계산한다.

A, B = map(int,input().split())

a_scale = -1
b_scale = -1
input_value = A
sum_length = 0
sum_total = 0
fromA = 0
toB = 0

def sumConverter(scale):
    global sum_length, sum_total
    prev = sum_total
    sum_total = 1 + sum_length + sum_total + prev
    sum_length = sum_length + 2**scale
    # print('sum', sum_length, sum_total)

def countDetail(scale):
    # print('SCALE!', scale)
    # 해당 scale 부터 카운트를 해야한다.
    startNumber = 2**scale
    targetNumber = input_value
    cnt = 0
    for cntNumber in range(startNumber, targetNumber + 1):
        if input_value == A and cntNumber == input_value:
            break
        # print('이곳에 1의 개수를 세는 로직', cntNumber, bin(cntNumber)[2:])
        cntNumBin = bin(cntNumber)[2:]
        for idx in range(len(cntNumBin)):
            if cntNumBin[idx] == '1':
                cnt += 1
    # print('TOTAL!!!!', cnt)
    return cnt

def checkValue(numb, scale):
    if 2**scale <= numb < 2**(scale+1):
        return True
    return False

def dfs(scale):
    # print(scale)
    global input_value, a_scale, b_scale, fromA, toB
    canIContinue = checkValue(input_value, scale)
    if canIContinue == True:
        if input_value == B:
            b_scale = scale
            pivot = countDetail(scale)
            toB = pivot + sum_total
            return
        elif input_value == A:
            a_scale = scale
            pivot = countDetail(scale)
            fromA = pivot + sum_total
            input_value = B

    sumConverter(scale)
    dfs(scale + 1)

dfs(0)
# print(fromA, toB, 'FROMATOB')
print(toB - fromA)
