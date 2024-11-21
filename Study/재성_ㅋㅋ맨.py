class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i, j = 0, 0
        ans = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
            j += 1
        
        return ans
