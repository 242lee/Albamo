"""
영어로만 이루어진 어떤 문서를 검색하는 함수를 만들려고 함
이 함수는 어떤 단어가 총 몇번 등장하는지 셈
중복되지 않게 해야함

검색하려는 단어가 최대 몇 번 중복되지않게 등장하는지 구하라

첫째 줄에 문서가 주어진다. 문서의 길이는 최대 2500이다. 둘째 줄에 검색하고 싶은 단어가 주어진다.
이 길이는 최대 50이다. 문서와 단어는 알파벳 소문자와 공백으로 이루어져 있다.
"""

doc = input().strip()
word = input().strip()

doc_len = len(doc)
word_len = len(word)

count = 0
i = 0

while i <= doc_len - word_len:
    if doc[i:i + word_len] == word:
        count += 1
        i += word_len   # 단어 길이만큼 건너뛰기
    else:
        i += 1  # 다르면 다음 글자로 이동

print(count)