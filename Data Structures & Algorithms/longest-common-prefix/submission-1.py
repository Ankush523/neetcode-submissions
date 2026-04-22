class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        longest_substr = ""

        for i in range(len(first_word)):
            char_to_check = first_word[i]

            for word in strs:
                if i==len(word) or word[i] != char_to_check:
                    return longest_substr
                
            longest_substr += char_to_check

        return longest_substr