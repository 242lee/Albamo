'''
case 개수 T
출발 x y 도착 x y
행성계의 개수 n
중점과 반지름 cx cy r

어린 왕자가 거쳐야 할 최소의 행성계 진입/이탈 횟수를 출력
'''
T = int(input())

for _ in range(T):
    sx, sy, ex, ey = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        rr = r * r
        
        d1d1 = (sx - cx) ** 2 + (sy - cy) ** 2
        d2d2 = (ex - cx) ** 2 + (ey - cy) ** 2
        
        if (d1d1 < rr and d2d2 > rr) or (d1d1 > rr and d2d2 < rr):
            cnt += 1
    
    print(cnt)