str = input()
word = input()

count = 0
length = len(word)
while str.find(word) != -1:
    n = str.find(word)
    str = str[n + length :]
    count += 1

print(count)