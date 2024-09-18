def solution(dirs):
    answer = 0
    move = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    visited = set()  
    now = (0, 0) 

    for dir in dirs:
        i, j = now
        di, dj = move[dir]
        ni, nj = i + di, j + dj
        
        if -5 <= ni <= 5 and -5 <= nj <= 5:
            # 경로 저장: 양방향으로 저장 (현재 좌표 -> 다음 좌표, 다음 좌표 -> 현재 좌표)
            if ((i, j), (ni, nj)) not in visited:
                visited.add(((i, j), (ni, nj))) 
                visited.add(((ni, nj), (i, j))) 
                answer += 1
            now = (ni, nj)

    return answer