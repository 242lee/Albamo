import sys
n = int(sys.stdin.readline().rstrip()) # 그냥 input으로 받으니까 시간 초과 남 ;;
result = set() # 중복 제거

for _ in range(n):
    com = sys.stdin.readline().split() 
    if len(com)==1: # 명령어 뒤에 x 가 없을 경우 (all, empty)
        if com[0] == 'all' :
            result = set([k for k in range(1, 21)])
        else :
            result = set() # 비워버려
    else :
        cd, x = com[0], int(com[1]) # 명령어와 뒤의 숫자 
        if cd == 'add' :
            result.add(x) # 추가해
        elif cd == 'remove' :
            result.discard(x) # 지워
        elif cd == 'check' : # 있으면 1 없으면 0
              if x in result: 
                  print(1)
              else: 
                  print(0)
        elif cd == 'toggle' : # 있으면 제거 없으면 추가
            if x in result :
                result.discard(x)
            else :
                result.add(x)