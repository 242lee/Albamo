# 455. Assign Cookies
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i = j = ans = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1

        return ans


g = [1,2,3]
s = [1,1]
a = Solution()
print(a.findContentChildren(g,s))