import sys
input = sys.stdin.readline


s = 0
for _ in range(int(input())):
    command, *num = input().split()
    if num:
        num = int(num[0])
        if command == 'add':
            s |= (1 << num)
        elif command == 'remove':
            s &= ~(1 << num)
        elif command == 'check':
            print(int(bool(s & (1 << num))))
        elif command == 'toggle':
            s ^= (1 << num)
    else:
        if command == 'all':
            s = 2097151
        elif command == 'empty':
            s = 0
