# LeetCode 11. Container With Most Water
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        s, e = 0, len(height)-1
        ans = 0
        while s < e:
            if height[s] < height[e]:
                h = height[s]
                s += 1
            else:
                h = height[e]
                e -= 1
            ans = max(ans, h*(e-s+1))

        return ans

height = [1,8,6,2,5,4,8,3,7]
a = Solution()
print(a.maxArea(height))