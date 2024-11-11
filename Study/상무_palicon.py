# 같은 알파벳이 몇개 있는지 구한다.
# 

class Solution:
  def longestPalindrome(self, s: str) -> int:
    result = 0
    letter_length = len(s)
    dict = {}

    for index in range(letter_length):
      if s[index] not in dict:
        dict[s[index]] = 1
      else:
        dict[s[index]] += 1

    odd_number = False
    for counts in dict:
      result += (dict[counts] // 2) * 2
      if dict[counts] % 2 == 1:
        odd_number = True
    
    if odd_number:
      result += 1
    
    return result

solution = Solution()
print(solution.longestPalindrome("abccccdd"))