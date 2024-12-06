def count_remaining_ones(n, m, forest, attacks):
    # 각 행의 1의 개수를 세어 리스트에 저장
    one_counts = [row.count(1) for row in forest]

    # 공격 범위에 따라 각 행의 1의 개수를 감소
    for start, end in attacks:
        for i in range(start - 1, end):  # 입력은 1-based이므로 0-based로 변환
            if one_counts[i] > 0:
                one_counts[i] -= 1

    # 남아있는 1의 개수의 합을 반환
    return sum(one_counts)

# 입력 처리
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    forest = []
    for i in range(n):
        row = list(map(int, data[index:index + m]))
        forest.append(row)
        index += m
    
    attacks = []
    for i in range(2):  # 공격은 항상 2번 주어진다고 가정
        start = int(data[index])
        end = int(data[index + 1])
        attacks.append((start, end))
        index += 2
    
    # 결과 계산
    result = count_remaining_ones(n, m, forest, attacks)
    
    # 결과 출력
    print(result)

if __name__ == "__main__":
    main()
