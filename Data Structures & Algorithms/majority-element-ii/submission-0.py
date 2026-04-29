from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        result = []
        for i in count:
            if count[i] > n/3 :
                result.append(i)
        return result