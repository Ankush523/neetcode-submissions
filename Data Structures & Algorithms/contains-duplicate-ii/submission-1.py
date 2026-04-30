class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i,val in enumerate (nums):
            print(i,val)
            if nums[i] not in freq:
                freq[val] = i
            else:
                diff = abs(i-freq[val])
                freq[val] = i
                if diff <= k:
                    return True
        print(freq)
        return False
