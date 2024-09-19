# 모든 수들을 + - 해본 경우의 수
# 트리구조 형태로 나타나게 됨

def solution(numbers, target):
  results = [0]            
  cnt = 0 

  for num in numbers : 
    temp = [] 
	
    for result in results: 
      temp.append(result + num)    
      temp.append(result - num)   
      # 더하고 뺀 경우의 수를 넣어버려 

    results = temp 
 
  for result in results : 
    if result == target : 
      cnt += 1

  return cnt