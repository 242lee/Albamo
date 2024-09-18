def solution(n, a, b):
    answer = 0
    p1 = a
    p2 = b

    while True:
        if p1 == p2:
            break
        p1 = ((p1 - 1) // 2) + 1
        p2 = ((p2 - 1) // 2) + 1
        answer += 1
    return answer

# print(solution(8, 1, 8))
