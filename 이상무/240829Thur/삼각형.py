# while True:
#     triangle = set(map(int, input().split()))
#     if triangle == [0]:
#         break
#     if len(triangle) == 1:
#         print('정삼각형')
#     elif len(triangle) == 2:
#         print('이등변삼각형')
#     else:
#         print('그냥 삼각형')

while True:
  a, b, c = map(int, input().split())
  if a == b == c == 0:
    break
  if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)):
    print("Invalid")
  elif a == b == c:
    print('Equilateral')
  elif a == b or b == c or a == c:
    print("Isosceles")
  else:
    print("Scalene")