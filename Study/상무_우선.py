# I 숫자 = 큐에 주어진 숫자 삽입
# D 1 = 큐에서 최댓값 삭제
# D -1 = 큐에서 최솟값 삭제

def solution(operations):
    queue = []

    for operate in operations:
        action, number = map(str, operate.split())
        if action == "I":
            queue.append(int(number))
        
        else:
            if not queue:
                continue
            if number == "1":
                queue.sort()
                queue.pop()
            else:
                queue.sort(reverse=True)
                queue.pop()
    
    if not queue:
        queue = [0, 0]

    return [max(queue), min(queue)]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
