'''
어떤 단어가 총 몇 번 등장하는 지
중복 안됨
앞에서부터 조회
최대 몇번 등장하는 지
'''

st = input() # 문장 받아
word = input() # 단어 받아
result = 0 # 최대 숫자 초기화
i = 0 # 어디서 부터 단어 찾기 시작할 지

while i <= len(st) - len(word): # 범위를 넘어가지 않는 동안
    if st[i:i+len(word)] == word: # 문장에서 탐색한 범위의 인덱스가 단어랑 같으면
        result += 1 # 결과에 카운트
        i += len(word) # 그 단어 뒤부터 다시 탐색
    else:
        i += 1 # 틀리면 바로 옆 인덱스부터 탐색

print(result)

