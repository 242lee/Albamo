from collections import deque
import sys
input = sys.stdin.readline

truck_amount, bridge_length, max_weight = map(int, input().split())
trucks = list(map(int, input().split()))

for i in range(bridge_length + 1):
    trucks.append(-1)

time = 1
curTruck = 1

q = deque()
q.append(trucks[0])
qSize = trucks[0]

while q:
    if len(q) == bridge_length:
        x = q.popleft()
        if x != -1:
            qSize -= x
    if qSize + trucks[curTruck] > max_weight:
        q.append(-1)
    else:
        q.append(trucks[curTruck])
        if trucks[curTruck] != -1:
            qSize += trucks[curTruck] 
        curTruck+=1
    time += 1
    if(qSize == 0): break

print(time)