"""
def backtrack

단어를 문자 단위로 찾음
현재 위치에서 상하좌우 방향으로 탐색, 이미 방문한 셀은 '#'로 표시 -> 재방문 방지

단어를 찾으면 탐색 중단
"""

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        result = set()

        def backtrack(r, c, word, index):
            if index == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if backtrack(r + dr, c + dc, word, index + 1):
                    board[r][c] = temp  
                    return True

            board[r][c] = temp
            return False

        for word in words:
            for r in range(rows):
                for c in range(cols):
                    if backtrack(r, c, word, 0):
                        result.add(word)
                        break  

        return list(result)
