class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i,val in enumerate(nums):
            if (i>0 and val == nums[i-1]):
                continue
            j=i+1
            for j in range(i + 1, len(nums)):
                if (j>i+1 and nums[j] == nums[j-1]):
                    continue
                left = j+1
                right = len(nums)-1
                new_target = target - (nums[i] + nums[j])
                while left<right:
                    if (nums[left] + nums[right] > new_target):
                        right -=1
                    elif (nums[left] + nums[right] < new_target):
                        left +=1
                    else:
                        result.append([val,nums[j],nums[left],nums[right]])
                        left +=1
                        right -=1
                        while (left<right and nums[left]==nums[left-1]):
                            left +=1
        return result