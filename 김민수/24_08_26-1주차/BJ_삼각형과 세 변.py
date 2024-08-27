"""
삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우
단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.

각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.
"""
while True:
    side_list = list(map(int, input().split()))

    # 입력이 0 0 0 이면 종료
    if side_list == [0, 0, 0]:
        break

    side_list.sort()  # 변의 길이를 오름차순으로 정렬

    # 삼각형이 안되는 경우
    if side_list[2] >= side_list[0] + side_list[1]:
        result = 'Invalid'
    # 삼각형이 되는 경우
    else:
        # 모든 변의 길이가 같은 경우
        if side_list[0] == side_list[1] == side_list[2]:
            result = 'Equilateral'
        # 두 변의 길이만 같은 경우
        elif side_list[0] == side_list[1] or side_list[1] == side_list[2]:
            result = 'Isosceles'
        # 모든 변의 길이가 다른 경우
        else:
            result = 'Scalene'

    print(result)

