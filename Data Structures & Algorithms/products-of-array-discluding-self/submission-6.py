class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_prod = 1
        result = [0] * len(nums)
        count = 0
        for i in range(0, len(nums)):
            if(nums[i]!=0):
                all_prod = all_prod * nums[i]
            else: 
                count+=1
        

        for j in range(0,len(nums)):
            if count == 0:
                result[j] = all_prod // nums[j]
            else:
                if(nums[j] != 0 or count>1):
                    result[j] = 0
                else:
                     result[j] = all_prod
        print(result)

        return result
