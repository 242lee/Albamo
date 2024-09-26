'''
다 탐색해버리겠다
'''

n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]
l = min(n,m)

result = 1

for i in range(n):
    for j in range(m):
        for k in range(1,l):
            if i+k<n and j+k<m:
                if (arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]):
                    result = max(result, k+1)

print(result*result)

