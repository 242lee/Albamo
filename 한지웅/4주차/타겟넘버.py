result = 0

def dfs(idx, mx_idx, current, target, numbers):
    global result
    # 정지조건 1: 현재 값이 목표치보다 작고, 남은 것들의 모든 합이 목표치와 현재값의 차이보다 작다면
    # 정지조건 2: 현재 값이 목표치보다 크고, 남은 것들의 모든 합(뺄꺼임)이 목표치와 현재값의 차이보다 작다면
    # 이 경우엔 더 진행할 필요가 없음!
    if idx == mx_idx:
        if current == target:
            result += 1
            return
        return
    # 정지조건 1, 2
    if (target - current) > 0 or (target - current) < 0:
        pivot = sum(numbers[idx+1:])
        if pivot < target - current:
            return

    dfs(idx + 1, mx_idx, current + numbers[idx+1], target, numbers)
    dfs(idx + 1, mx_idx, current - numbers[idx+1], target, numbers)
    return

def solution(numbers, target):
    # answer = 0
    dfs(0,len(numbers)-1, numbers[0], target, numbers)
    dfs(0,len(numbers)-1, -numbers[0], target, numbers)
    # print(result)
    return result
