from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dictionary = Counter(nums)
        print(dictionary)
        for i,key in enumerate(dictionary):
            if (dictionary[key] > n/2) : 
                return key
