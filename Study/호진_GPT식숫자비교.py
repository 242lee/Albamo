import sys
input = sys.stdin.readline

n = int(input())
numbers = [input().strip() for _ in range(n)]

def sort_key(num):
    if '.' in num:
        x, y = num.split('.')
        x = int(x)
        y = int(y)  # 소수점 뒤의 값을 정수로 취급
    else:
        x = int(num)
        y = -1  # 소수점이 없는 경우 소수부를 -1로 설정 (항상 더 작게 취급)
    return (x, y)

sorted_numbers = sorted(numbers, key=sort_key)

print(*sorted_numbers, sep='\n')