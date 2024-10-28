# 백준 32371 샷건 브1
import sys
input = sys.stdin.readline

keyboard = [input().rstrip() for _ in range(4)]
shotgun = input().rstrip()

set_i = set()
set_j = set()

for s in shotgun:
    for i in range(4):
        for j in range(10):
            if keyboard[i][j] == s:
                set_i.add(i)
                set_j.add(j)

target = [
    (max(set_i) + min(set_i)) // 2, 
    (max(set_j) + min(set_j)) // 2
]

print(keyboard[target[0]][target[1]])