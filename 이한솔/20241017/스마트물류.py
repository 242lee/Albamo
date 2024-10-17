'''
리스트로 만들어
로봇 위치를 돌면서 n-k 의 부품부터 확인해
잡을 수 있으면 +1 
'''

n, k = map(int, input().split())
arr = list(map(str, input()))

result = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(i-k,i+k+1):
            if (i==j) or (0>j) or (j>=n): 
                continue
            if arr[j] == 'H':
                arr[j] = 'N'
                result += 1
                break

print(result)
            


  