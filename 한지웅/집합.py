import sys

# import sys해서 받아야 하고 (시간초과)
# deepcopy를 쓰면 메모리 초과

N = int(input())

lst = set()


for _ in range(N):
    input = sys.stdin.readline().strip().split()

    if len(input) == 1:
        if input[0] == 'all':
            lst = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
        else:
            lst.clear()
    else:
        order = input[0]
        num = input[1]
        if order == 'add':
            # add
            # if num not in lst:
            lst.add(num)
        elif order == 'check':
            # check
            if num in lst:
                print('1')
            else:
                print('0')
        elif order == 'remove':
            # remove
            if num in lst:
                lst.remove(num)
        else:
            # toggle
            if num in lst:
                lst.remove(num)
            else:
                lst.add(num)
