from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_table = Counter(nums)
        missing_vals = []
        max_val = max(hash_table)
        if (max_val < 0):
            return 1
        else:
            for i in range(1, max_val+2):
                if i not in hash_table:
                    return i
        
