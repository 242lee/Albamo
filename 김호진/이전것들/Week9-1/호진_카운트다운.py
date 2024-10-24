# 프로그래머스 카운트 다운

def solution(target):
    answer = [0, 0]

    if 120 <= target:
        answer[0] += target // 60 - 1
        target -= 60 * (target // 60 - 1)

    if 110 < target < 120:
        answer[0] += 3
        answer[1] += 3

    if target == 110:
        answer[0] += 2
        answer[1] += 1

    if 100 < target < 110:
        if (target - 60) % 3 == 0:
            target -= 60
            answer[0] += 1
        else:
            answer[0] += 3
            answer[1] += 3

    if target == 100:
        answer[0] += 2
        answer[1] += 2

    if 90 < target < 100:
        if (target - 60) % 2 == 0 or (target - 60) % 3 == 0:
            target -= 60
            answer[0] += 1
        else:
            answer[0] += 3
            answer[1] += 3

    if 80 < target <= 90:
        if (target - 50) % 2 == 0 or (target - 50) % 3 == 0:
            target -= 50
            answer[0] += 1
            answer[1] += 1
        else:
            target -= 60
            answer[0] += 1

    if 70 < target <= 80:
        answer[0] += 2
        answer[1] += 1
    
    if 60 < target <= 70:
        answer[0] += 2
        answer[1] += 2

    if target == 60:
        target -= 60
        answer[0] += 1

    if 50 <= target < 60:
        if target % 3 == 0:
            answer[0] += 1
        else:
            target -= 50
            answer[0] += 1
            answer[1] += 1
    
    if 40 < target < 50:
        if target % 3 == 0:
            answer[0] += 1
        else:
            target -= 40
            answer[0] += 1

    if 20 < target <= 40:
        if target % 2 == 0 or target % 3 == 0:
            answer[0] += 1
        else:
            target -= 20
            answer[0] += 1
            answer[1] += 1

    if 0 < target <= 20:
        answer[0] += 1
        answer[1] += 1

    return answer

# for i in range(81, 171):
#     print(i, solution(target=i))
# print(solution(target=21))
# print(solution(target=58))
for i in range(1, 201):
    print(i, solution(target=i))
