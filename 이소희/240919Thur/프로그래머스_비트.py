def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            bin_num = list('0' + bin(num)[2:]) 
            # 가장 작은 값을 구해야 하므로 뒤에서부터 
            for i in range(len(bin_num) - 1, -1, -1):
                if bin_num[i] == '0':
                    bin_num[i] = '1'
                    if i + 1 < len(bin_num):
                        bin_num[i + 1] = '0'
                    break
            answer.append(int(''.join(bin_num), 2))
    return answer

'''
만약 num = 3이라면 (즉, bin_num = ['0', '1', '1']):

루프는 오른쪽에서부터 순회
i = 2일 때, bin_num[2]는 1이므로 조건에 맞지 않음.
i = 1일 때, bin_num[1]는 1이므로 조건에 맞지 않음.
i = 0일 때, bin_num[0]는 0입니다. 이때 조건을 만족:
bin_num[0]를 1로 변경. 
리스트 : ['1', '1', '1']
'''
# 테스트
print(solution([2, 7]))  # [3, 11]
