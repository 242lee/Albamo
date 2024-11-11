def solution(order):
    stack = []
    idx = 0
    box = 1
    n = len(order)

    # 컨테이너 벨트에서 상자를 하나씩 가져오면서 처리
    while box <= n:
        if box == order[idx]:
            idx += 1
        else:
            stack.append(box)
        box += 1

        # 보조 컨테이너 벨트에서 실을 수 있는 상자를 실음
        while stack and stack[-1] == order[idx]:  
            stack.pop()
            idx += 1

    return idx
