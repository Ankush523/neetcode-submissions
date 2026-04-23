from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s = Counter(s)
        char_count_t = Counter(t)
        if char_count_s == char_count_t:
            return True
        return False