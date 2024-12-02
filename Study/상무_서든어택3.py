import sys
input = sys.stdin.readline

N = int(input())
users = list(map(int, input().split()))

me = users[0]
enemies = sorted(users[1:])

for enemy in enemies:
    if me <= enemy:
        print('No')
        break
    me += enemy
else:
    print('Yes')