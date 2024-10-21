def solution(sequence):
    n = len(sequence)
    
    # 펄스 수열 1: [1, -1, 1, -1, ...]
    pulse1 = [1 if i % 2 == 0 else -1 for i in range(n)]
    # 펄스 수열 2: [-1, 1, -1, 1, ...]
    pulse2 = [-1 if i % 2 == 0 else 1 for i in range(n)]
    
    # 펄스 수열 1을 곱한 결과 수열
    pulse1_sequence = [sequence[i] * pulse1[i] for i in range(n)]
    # 펄스 수열 2를 곱한 결과 수열
    pulse2_sequence = [sequence[i] * pulse2[i] for i in range(n)]
    
    # Kadane's Algorithm을 적용하여 두 수열에서 최대 연속 부분 합을 찾음
    def max_subarray_sum(arr):
        current_sum = 0
        max_sum = float('-inf')
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    # 두 가지 펄스 수열에 대해 최대 연속 부분 합 계산
    max_sum_pulse1 = max_subarray_sum(pulse1_sequence)
    max_sum_pulse2 = max_subarray_sum(pulse2_sequence)
    
    # 두 값 중 더 큰 값을 반환
    return max(max_sum_pulse1, max_sum_pulse2)
