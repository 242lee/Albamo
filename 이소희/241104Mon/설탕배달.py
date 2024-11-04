N = int(input())

def min_sugar_bags(N):
    count = 0
    while N >= 0:
        if N % 5 == 0: 
            count += N // 5
            return count
        N -= 3 
        count += 1  
    return -1  

print(min_sugar_bags(N))
