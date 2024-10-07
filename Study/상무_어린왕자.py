# x1, y1 -> x2, y2로 이동해야한다.
# 점의 좌표와 반지름의 길이 r을 줬을 때 
# e.g.) 점의 좌표 = (a, b)
# (x1 - a)^2 + (y1 - b)^2 <= r^2 이 성립하는 원과
# (x2 - a)^2 + (y2 - b)^2 <= r^2 이 성립하는 원의 좌표를
# set() 메서드에 넣고 set()의 길이를 result로 받아와서 풀이하고 싶음

def count_planet(x1, y1, x2, y2, planets):
    count = 0
    planet_states = set()  # 행성계의 진입/이탈 횟수를 저장할 집합

    for cx, cy, r in planets:
        # 원의 방정식으로 점이 원 안에 있는지 체크
        is_x1_inside = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2
        is_x2_inside = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2
        
        if is_x1_inside != is_x2_inside:
            planet_states.add((cx, cy, r))
    
    # 진입/이탈 횟수는 행성계의 개수
    count = len(planet_states)
    
    return count

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    
    planets = []
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        planets.append((cx, cy, r))
    
    result = count_planet(x1, y1, x2, y2, planets)
    print(result)
