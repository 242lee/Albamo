import sys
input = sys.stdin.readline

end = [0, 0, 0]

while True:
    arr = list(map(int, input().split()))
    if arr == end:
        break

    if arr[0] == arr[1] and arr[0] == arr[2]:
        print('Equilateral')
    elif arr[0] >= arr[1] + arr[2] or arr[1] >= arr[0] + arr[2] or arr[2] >= arr[0] + arr[1]:
        print('Invalid')
    elif arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
        print('Isosceles')
    else:
        print('Scalene')