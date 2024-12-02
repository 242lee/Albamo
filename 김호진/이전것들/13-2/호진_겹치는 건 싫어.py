# 백준 20922 겹치는 건 싫어 실1
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

bit = {}
for i in range(N):
    if arr[i] not in bit:
        bit[arr[i]] = 1
        
