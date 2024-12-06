# softeer

def gpt_sort(numbers):
    def gpt_key(number):
        # 소수점을 기준으로 정수부와 소수부를 분리
        if '.' in number:
            integer_part, fractional_part = number.split('.')
        else:
            integer_part, fractional_part = number, None  # 소수점이 없는 경우 소수부는 None으로 처리
        
        # 소수점 없는 경우를 가장 작게 처리하기 위해 소수부를 -1으로 반환
        return (int(integer_part), int(fractional_part) if fractional_part is not None else -1)

    # GPT 기준에 따라 비내림차순 정렬
    sorted_numbers = sorted(numbers, key=gpt_key)
    return sorted_numbers

# 입력 처리
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    numbers = data[1:n+1]
    
    # GPT식으로 정렬
    sorted_numbers = gpt_sort(numbers)
    
    # 결과 출력
    for number in sorted_numbers:
        print(number)

if __name__ == "__main__":
    main()
