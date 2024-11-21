class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        length = len(s)
        
        for i in range(len(g)):
            for j in range(len(s)):
                if g[i] <= s[j]:
                    result += 1
                    s.remove(s[j])
                    break
        return result