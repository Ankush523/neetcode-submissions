from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dictionary = Counter(nums)
        print(dictionary)
        for i,val in enumerate(dictionary):
            if (dictionary[val] > n/2) : 
                return val
