# 저 사이트에서 코드가 안돌아가요.
word_dictionary = {}
words = input()
for word in words:
    word_dictionary[word] = word_dictionary.get(word, 0) + 1

length = 0
odd = False
for cnt in word_dictionary.values():
    length += ( cnt // 2 ) * 2
    if cnt % 2 == 1 and odd == False:
        length += 1
        odd = True

print(length)
