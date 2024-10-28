import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

arr = [list(input().strip())for l in range(4)]
target = set(input().strip())

x = 0
y = 0

for i in range(4):
    for j in range(10):
        for t in target:
            if arr[i][j] == t:
                x += i
                y += j

print(arr[x//9][y//9])
