from collections import deque

def solution(operations):
    answer = []
    dq = deque()
    
    for operation in operations:
        op, val = operation.split()
        val = int(val)
        
        if op == "I":
            dq.append(val)
        elif op == "D" and dq:
            if val == 1:
                dq.remove(max(dq))
            elif val == -1:
                dq.remove(min(dq))
    
    if dq:
        answer = [max(dq), min(dq)]
    else:
        answer = [0, 0]
    
    return answer
