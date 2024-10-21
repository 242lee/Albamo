def solution(sequence):
    answer = 0
    groupA = []
    groupB = []
    isPositive = 1
    maxASum = []
    maxBSum = []
    for i in sequence:
        nextA = i * isPositive
        nextB = i * (-1) * isPositive
        groupA.append(nextA)
        groupB.append(nextB)
        if len(maxASum) == 0:
            maxASum.append(nextA)
            maxBSum.append(nextB)
            answer = max(nextA, nextB)
            isPositive *= -1
            continue
        else:
            newNextA = max(nextA, nextA + maxASum[-1])
            newNextB = max(nextB, nextB + maxBSum[-1])
            if newNextA > answer:
                answer = newNextA
            if newNextB > answer:
                answer = newNextB
            maxASum.append(newNextA)
            maxBSum.append(newNextB)
            isPositive *= -1
            continue
    
    return answer



# print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
