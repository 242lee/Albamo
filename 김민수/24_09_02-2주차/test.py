from itertools import groupby

# 입력값을 공백이 있는것과 없는것을 기준으로 받는 함수

def findblank(doc):
    # 공백이 있는 경우
    if ' ' in doc:
        return doc.split()
    # 공백이 없는 경우 연속된 문자 그룹화
    else:
        return list(doc)

doc = input()
word = input()
doc_list = findblank(doc)
word_list = findblank(word)
length_difference = len(doc_list) - len(word_list)
result = 0
visited = [0] * len(doc_list)

for i in range(0, length_difference + 1):
    cnt = 0
    for j in range(len(word_list)):
        if doc_list[i+j] == word_list[j] and visited[i+j] == 0:
            cnt += 1
        else:
            break

    if cnt == len(word_list):
        result += 1
        for j in range(len(word_list)):
            visited[i+j] = 1

print(result)
