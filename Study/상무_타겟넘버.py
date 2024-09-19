# 처음 숫자를 0으로 설정하고 numbers에서 num을 받아서 +, - 한 값들을 append해준다.
# 그걸 2^n의 시간복잡도로 풀이한 후 target에 해당하면 answer값을 1씩 더해주고 answer을 return 한다.

def solution(numbers, target):
    answer = 0
    sum_of_numbers = [0]

    for num in numbers:
        tmp = []
        for previous_sum in sum_of_numbers:
            tmp.append(previous_sum + num)
            tmp.append(previous_sum - num)
        sum_of_numbers = tmp
        
    for num in sum_of_numbers:
        if num == target:
            answer += 1
            
    return answer