def bt(numbers, n, sum, last, target):
    global answer
    if last == n-1:
        if sum == target:
            answer += 1
        return
    i = last + 1
    bt(numbers, n, sum+numbers[i], i, target)
    bt(numbers, n, sum-numbers[i], i, target)


def solution(numbers, target):
    global answer
    answer = 0
    n = len(numbers)
    bt(numbers, n, 0, -1, target)
    
    return answer
