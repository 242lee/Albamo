import sys

def gpt_sort_key(value):
    """
    GPT의 기준에 따라 숫자를 비교하기 위한 키를 반환.
    - 소수점 기준으로 나누어 왼쪽 부분(x), 오른쪽 부분(y)을 따로 처리.
    - 소수점이 없는 경우 y를 빈 문자열로 설정.
    """
    if '.' in value:
        x, y = value.split('.')
    else:
        x, y = value, ''  # 소수점 없는 경우 y는 빈 문자열.
    return (int(x), len(y), y)  # x값은 정수로, y값은 길이와 문자열 순서로 비교.

def main():
    input = sys.stdin.readline  # 표준 입력 함수.
    N = int(input().strip())  # 첫 번째 줄에서 N 읽기.
    numbers = [input().strip() for _ in range(N)]  # 다음 N개의 줄에서 숫자 읽기.
    
    # GPT 기준에 따라 정렬. gpt_sort_key를 키 함수로 사용.
    sorted_numbers = sorted(numbers, key=gpt_sort_key)
    
    # 결과 출력.
    print('\n'.join(sorted_numbers))

if __name__ == "__main__":
    main()
