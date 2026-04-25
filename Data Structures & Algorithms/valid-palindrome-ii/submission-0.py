class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = ''
        right = ''
        if list(s) == list(reversed(s)):
            return True
        else:
            right = len(s)-1
            left = 0
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    if s[left+1:right+1] == s[left+1:right+1][::-1]:
                        return True
                    elif (s[left:right] == s[left:right][::-1]):
                        return True
                    else:
                        return False