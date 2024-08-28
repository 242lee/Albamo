'''
메모리 31120KB 시간 32ms
'''

while True:
    lst = list(map(int, input().split()))
    lst.sort()

    if lst[0] == lst[1] == lst[2] == 0:
        break

    # 삼각형의 조건을 만족하는 경우
    if lst[0] + lst[1] > lst[2]:

        # 두 변 이상 같은 경우
        if (lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]):
            if lst[0] == lst[1] == lst[2]:
                print('Equilateral')
            else:
                print('Isosceles')
        else:
            print('Scalene')
    
    else:
        print('Invalid')

    