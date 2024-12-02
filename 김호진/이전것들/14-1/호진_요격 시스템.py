# 프로그래머스 요격 시스템

def solution(targets):
    answer = 0
    targets.sort()
    i = 0
    while i < len(targets):
        s, e = targets[i][0], targets[i][1]
        j = i + 1
        while j < len(targets) and targets[j][0] < e:
            j += 1
        i += j
        answer += 1
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))
