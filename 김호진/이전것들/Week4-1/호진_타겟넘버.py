# 프로그래머스
# 타겟 넘버

# 평범한 조합 문제였다. (함수명을 dfs라고 썼지만 바꾸기 귀찮)

def solution(numbers, target):
    global answer
    answer = 0
    num = sum(numbers)
    dfs(numbers, target, num, 0)
    return answer

def dfs(numbers, target, num, i):
    global answer
    if num == target:
        answer += 1
        return
    if num < target:
        return
    if i == len(numbers):
        return
    dfs(numbers, target, num-numbers[i]*2, i+1)
    dfs(numbers, target, num, i+1)


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))