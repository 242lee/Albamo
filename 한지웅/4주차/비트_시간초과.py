def number_vs(main_num, another_num):
    # 번호 두개를 비교하는 과정.
    bin_main = bin(main_num)[2:]
    bin_another = bin(another_num)[2:]
    mx_len = len(bin_another)
    if len(bin_main) < mx_len:
        bin_main = '0' * (mx_len - len(bin_main)) + bin_main

    diff = 0
    for _ in range(mx_len):
        if bin_main[_] != bin_another[_]:
            diff += 1
            if diff > 2:
                return False
    return True

def define_push_numb(main_num):
    # 번호를 입력하면, 그 번호에 해당하는 정답을 뽑아내는 함수
    target = main_num + 1
    while True:
        result = number_vs(main_num, target)
        if result == True:
            return target
        else:
            target += 1

def solution(numbers):
    answer = []
    for _ in range(len(numbers)):
        answer += [define_push_numb(numbers[_])]
    return answer
