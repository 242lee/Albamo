# LeetCode 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        pal = {}
        for letter in s:
            pal[letter] = pal.get(letter, 0) + 1

        ans = 0
        has_odd = False
        for num in pal.values():
            if num % 2 == 1:
                has_odd = True
                ans += num - 1
            else:
                ans += num

        return ans + int(has_odd)

s = "abccccdd"
a = Solution()
print(a.longestPalindrome(s))