'''
문제 설명
어떤 수열의 연속 부분 수열에 같은 길이의 펄스 수열을 각 원소끼리 곱하여 연속 펄스 부분 수열을 만들려 합니다. 펄스 수열이란 [1, -1, 1, -1 …] 또는 [-1, 1, -1, 1 …] 과 같이 1 또는 -1로 시작하면서 1과 -1이 번갈아 나오는 수열입니다.
예를 들어 수열 [2, 3, -6, 1, 3, -1, 2, 4]의 연속 부분 수열 [3, -6, 1]에 펄스 수열 [1, -1, 1]을 곱하면 연속 펄스 부분수열은 [3, 6, 1]이 됩니다. 또 다른 예시로 연속 부분 수열 [3, -1, 2, 4]에 펄스 수열 [-1, 1, -1, 1]을 곱하면 연속 펄스 부분수열은 [-3, -1, -2, 4]이 됩니다.
정수 수열 sequence가 매개변수로 주어질 때, 연속 펄스 부분 수열의 합 중 가장 큰 것을 return 하도록 solution 함수를 완성해주세요.

제한 사항
1 ≤ sequence의 길이 ≤ 500,000
-100,000 ≤ sequence의 원소 ≤ 100,000
sequence의 원소는 정수입니다.
입출력 예
sequence	result
[2, 3, -6, 1, 3, -1, 2, 4]	10
입출력 예 설명
주어진 수열의 연속 부분 수열 [3, -6, 1]에 펄스 수열 [1, -1, 1]을 곱하여 연속 펄스 부분 수열 [3, 6, 1]을 얻을 수 있고 그 합은 10으로서 가장 큽니다.

'''
# 풀이 1 어디서 틀린지 몰라서 다시 다듬어서 풀기 시작.
# def solution(sequence):
#     answer = 0

#     first_pulse_sequence = []
#     second_pulse_sequence = []

#     for i in range(len(sequence)):
#         first_pulse_sequence.append(sequence[i] * (-1) ** i)
#         second_pulse_sequence.append((sequence[i] * (-1) ** i) * (-1))
    
#     first_compare_sequence = []
#     second_compare_sequence = []
#     for i in range(len(sequence)):
#         if i > 0:
#             first_compare_sequence.append(first_compare_sequence[i - 1] + first_pulse_sequence[i])
#             second_compare_sequence.append(second_compare_sequence[i - 1] + second_pulse_sequence[i])
#         else:
#             first_compare_sequence.append(first_pulse_sequence[0])
#             second_compare_sequence.append(second_pulse_sequence[0])
    
#     max_first = max(first_compare_sequence) - min(first_compare_sequence)
#     max_second = max(second_compare_sequence) - min(second_compare_sequence)

#     answer = max(max_first, max_second)
#     return answer


# 풀이 2
# 펄스가 총 2개이다 [1, -1, 1, -1 ...], [-1, 1, -1, 1 ...]
# 그래서 sequence에 펄스들을 곱해서 두개로 만들어서 부분수열의 최대값을 구한다.
# 왼쪽을 순회하면서 부분합을 구해준다.
# 근데 부분합이 음수가 되면 다음 합이 이전 부분합보다 작아지므로 새로운 부분수열을 시작한다.

def solution(sequence):
    first_pulse_sequence = [sequence[i] * (-1) ** i for i in range(len(sequence))]
    second_pulse_sequence = [sequence[i] * (-1) ** (i + 1) for i in range(len(sequence))]

    def max_subarray_sum(arr):
        current_sum = max_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    max_first_sum = max_subarray_sum(first_pulse_sequence)
    max_second_sum = max_subarray_sum(second_pulse_sequence)

    return max(max_first_sum, max_second_sum)