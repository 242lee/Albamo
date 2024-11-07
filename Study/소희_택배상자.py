def solution(order):
    sub = [] 
    cur = 1 
    cnt = 0

    for o in order:
        while cur <= len(order) and (not sub or sub[-1] != o):
            sub.append(cur)
            cur += 1

        if sub and sub[-1] == o:
            sub.pop() 
            cnt += 1 
        else:
            break

    return cnt
