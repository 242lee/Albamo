# 프로그래머스 카운트 다운

def solution(target):
    answer = [0, 0]

    if target > 70:
        if target % 60:
            target -= 60 * (target // 60)
            answer[0] += target // 60
        else:
            target -= 60 * (target // 60 - 1)
            answer[0] += target // 60 - 1

    if target > 50:
        target -= 50
        answer[0] += 1
        answer[1] += 1
    
    if target > 40:
        target -= 40
        answer[0] += 1

    if target > 20:
        target -= 20
        answer[0] += 1
        answer[1] += 1

    if target <= 20:
        answer[0] += 1
        answer[1] += 1

    return answer

print(solution(target=21))
print(solution(target=58))
