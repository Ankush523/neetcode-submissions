class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        word = ""
        while (left<=len(word1)-1 and right<=len(word2)-1):
            word = word + word1[left] + word2[right]
            left+=1
            right+=1
        print(word, left, right)
        while(left > len(word1)-1 and right <= len(word2)-1):
            word = word + word2[right]
            right+=1
        while (right > len(word2)-1 and left <= len(word1)-1):
            word = word + word1[left]
            left+=1
        return word