class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(k<len(nums)):
            nums.reverse()
            nums[0:k] = nums[0:k][::-1]
            nums[k:len(nums)] = nums[k:len(nums)][::-1]
        else:
            k = k%len(nums);
            nums.reverse()
            nums[0:k] = nums[0:k][::-1]
            nums[k:len(nums)] = nums[k:len(nums)][::-1]
        return nums
