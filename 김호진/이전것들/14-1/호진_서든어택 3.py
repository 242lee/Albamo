# 백준 22993 서든어택 3 실4
import sys
input = sys.stdin.readline

N = int(input())
me, *others = list(map(int, input().split()))

others.sort()
for other in others:
    if me <= other:
        print('No')
        break
    me += other
else:
    print('Yes')