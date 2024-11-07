def solution(order):
    answer = 0
    stack = []
    current_box = 1
    
    for target_box in order:
        # 현재 박스가 목표 박스보다 작으면 컨테이너 벨트에서 스택으로 이동
        while current_box <= target_box:
            stack.append(current_box)
            current_box += 1
            
        # 스택의 맨 위 상자가 목표 상자와 일치하면 트럭에 적재
        if stack and stack[-1] == target_box:
            stack.pop()
            answer += 1
        else:
            # 상자를 더 실을 수 없는 경우
            break
            
    return answer

# 예시
print(solution([4, 3, 1, 2, 5]))  # 2
print(solution([5, 4, 3, 2, 1]))  # 5