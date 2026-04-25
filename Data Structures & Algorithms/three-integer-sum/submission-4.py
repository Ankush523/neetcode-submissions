class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i,val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            target = -val
            while (j<k):
                if(nums[j] + nums[k] > target):
                    k=k-1
                elif(nums[j] + nums[k] < target):
                    j=j+1
                else:
                    result.append([val, nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        
        return result