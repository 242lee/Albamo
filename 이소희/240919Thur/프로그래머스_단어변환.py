from collections import deque

def solution(begin, target, words):
    # target이 words 리스트에 없는 경우
    if target not in words :
        return 0

    def bfs(w):
        q = deque()
        q.append((w, 0))
        
        visited = []  # 방문한 단어 집합
        visited.append(begin)
        
        while q:
            current_word, steps = q.popleft()
        
            if current_word == target:
                return steps

            for word in words:
                diff = 0
                for i in range(len(word)):
                    if current_word[i] != word[i]:
                        diff += 1
                # 아직 방문 안 했고, 1글자 차이나는게 맞으면
                if word not in visited and diff == 1:
                    visited.append(word)
                    q.append((word, steps + 1))
        return 0
    
    return bfs(begin)
    
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
'''
from collections import deque

def solution(begin, target, words):
    def is_next(word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff == 1
    
    def bfs(w):
        q = deque()
        q.append((w, 0))
        
        visited = []  # 방문한 단어 집합
        visited.append(begin)
        
        while q:
            current_word, steps = q.popleft()
        
            if current_word == target:
                return steps

            for word in words:
                if word not in visited and is_next(current_word, word):
                    visited.append(word)
                    q.append((word, steps + 1))
        return 0
                
    # target이 words 리스트에 없는 경우
    if target not in words :
        return 0
    
    return bfs(begin)
'''
        
        