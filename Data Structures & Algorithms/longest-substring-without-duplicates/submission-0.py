class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_res = 0
        char_set = set()
        for r in range(0,len(s)):
            while s[r] in char_set :
                char_set.discard(s[l])
                l+=1
            char_set.add(s[r])
            max_res = max(max_res,r-l+1)
        return max_res