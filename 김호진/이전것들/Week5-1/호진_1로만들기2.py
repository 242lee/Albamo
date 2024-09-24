# 백준 12852 1로 만들기 2 실1

import sys
input = sys.stdin.readline

n = int(input())

def dfs(num):
    if num == 1:
        global cnt, ans
        if cnt > len(op):
            cnt = len(op)
            ans = op[:]
        return
    
    if cnt <= len(op):
        return

    if num % 3 == 0:
        op.append(num//3)
        dfs(num//3)
        op.pop()
        
    if num % 2 == 0:
        op.append(num//2)
        dfs(num//2)
        op.pop()

    op.append(num-1)
    dfs(num-1)
    op.pop()

cnt = 10**9
ans = [n]
op = [n]
dfs(n)

print(cnt-1)
print(*ans)