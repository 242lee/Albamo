def solution(n, a, b):
    answer = 0
    
    while True:
        if a == b:
            break
        a = (a + 1) // 2  # a 참가자의 다음 라운드 번호
        b = (b + 1) // 2  # b 참가자의 다음 라운드 번호
        answer += 1       
        print(a, b)
    return answer
