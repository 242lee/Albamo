def solution(targets):
    result, end = 0, 0
    # print(sorted(targets, key = lambda x : x[1]))
    for s, e in sorted(targets, key = lambda x : x[1]):
        if s >= end:
            end = e
            result += 1
    
    return result


print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))