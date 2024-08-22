# 백준 1157 단어 공부 브1

word = input()
s = [0] * 26

for w in word:
    x = ord(w)
    if x <= 90:
        x -= 65
    else:
        x -= 97
    s[x] += 1

maximum = max(s)
most = s.index(maximum)
s[most] = 0
if maximum in s:
    print('?')
else:
    print(chr(most + 65))
