# 샷건
keyboard = []
for _ in range(4):
    row = list(input()) 
    keyboard.append(row) 

problem = input()

idx = []
for k in range(len(problem)): 
    found = False
    for i in range(4):
        for j in range(10):
            if problem[k] == keyboard[i][j]:
                idx.append((i, j)) 
                found = True
                break 
        if found:
            break 

average_i = round(sum(position[0] for position in idx) / len(idx)) 
average_j = round(sum(position[1] for position in idx) / len(idx)) 

print(keyboard[average_i][average_j])
