import sys
input = sys.stdin.readline

n = int(input())
numbers = [input() for _ in range(n)]

# GPT 기준 정렬 함수
def gpt_sort_key(num):
    if '.' in num:
        x, y = num.split('.')
        x = int(x)
        y = int(y)
    else:
        x = int(num)
        y = -1
    return (x, y)

sorted_numbers = sorted(numbers, key=gpt_sort_key)

for s in sorted_numbers:
    print(s)
