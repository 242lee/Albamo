# 백준 1051 숫자 정사각형 실3
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip("\n"))) for _ in range(n)]


def find_max_rect():
    min_len = min(n, m)
    for L in range(min_len-1, 0, -1):
        for i in range(n-L):
            for j in range(m-L):
                if arr[i][j] == arr[i][j+L] == arr[i+L][j] == arr[i+L][j+L]:
                    return (L+1)**2
    return 1

print(find_max_rect())
