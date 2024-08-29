# 백준 1543 문서 검색 실5
import sys
input = sys.stdin.readline

arr = input()
word = input()

n = len(arr) - 1
m = len(word) - 1
i = 0
res = 0
while i <= n-m:
    for j in range(m):
        if arr[i+j] != word[j]:
            break
    else:
        i += j
        res += 1
    i += 1

print(res)