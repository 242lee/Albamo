# 프로그래머스
# 예상 대진표

# 그냥 a/2, b/2해서 그 몫이 같아지면 만나는 거임
# 근데 첫 대진이 1, 2이면 몫이 1이랑 2랑 다르니까
# 0이랑 1이 첫 대진이도록 초기에 설정 해주면 됨
def solution(n,a,b):
    a -= 1
    b -= 1
    answer = 0
    while a != b:
        a //= 2
        b //= 2
        answer += 1

    return answer

print(solution(8, 4, 7))
