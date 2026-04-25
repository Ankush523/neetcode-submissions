class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = [char.lower() for char in s if char.isalnum()]
        if char_list == list(reversed(char_list)):
            return True
        return False