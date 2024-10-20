# 프로그래머스 연속 펄스 부분 수열의 합

# 시간초과 났음

def solution(sequence):
    N = len(sequence)
    pls = 1
    num1 = sequence[0] * pls
    num2 = sequence[0] * -pls
    was_positive_1 = num1 >= 0
    was_positive_2 = num2 >= 0

    sum_1 = []
    sum_2 = []
    part_ss_1 = num1
    part_ss_2 = num2
    for i in range(1, N):
        pls *= -1
        num1 = sequence[i] * pls
        num2 = sequence[i] * -pls

        if was_positive_1 == (num1 >= 0):
            part_ss_1 += num1
        else:
            sum_1.append(part_ss_1)
            part_ss_1 = num1
            was_positive_1 = not was_positive_1

        if was_positive_2 == (num2 >= 0):
            part_ss_2 += num2
        else:
            sum_2.append(part_ss_2)
            part_ss_2 = num2
            was_positive_2 = not was_positive_2

    sum_1.append(part_ss_1)
    sum_2.append(part_ss_2)

    ans = -100000

    for i in range(len(sum_1)):
        ss = 0
        for j in range(i, len(sum_1)):
            ss += sum_1[j]
            ans = max(ans, ss)

    for i in range(len(sum_2)):
        ss = 0
        for j in range(i, len(sum_2)):
            ss += sum_2[j]
            ans = max(ans, ss)

    return ans

print(solution(sequence=[2, 3, -6, 1, 3, -1, 2, 4]))
