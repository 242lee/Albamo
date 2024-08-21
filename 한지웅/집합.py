import sys
# 시간초과.
pivot_all = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
pivot = set()
N = int(input())
for _ in range(N):
    data = input()

    if data == 'all':
        pivot = pivot_all

    elif data == 'empty':
        pivot = pivot.clear()

    else:
        new_data = data.split(' ')
        order = new_data[0]
        num = new_data[1]
        check = num in pivot
        if order == 'add' and check == False:
            pivot.add(num)
        elif order == 'remove' and check == True:
            pivot.remove(num)
        elif order == 'toggle' and check == True:
            pivot.remove(num)
        elif order == 'toggle' and check == False:
            pivot.add(num)
        elif order == 'check' and check == True:
            print(1)
        elif order == 'check' and check == False:
            print(0)
        else:
            continue


