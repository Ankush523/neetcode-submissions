class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        min_val=100000
        sum_val=0
        while(j<len(nums)):
            sum_val = sum_val + nums[j]
            print("sum",sum_val)
            if(sum_val < target):
                j+=1
            else:
                min_val = min(min_val,j-i+1)
                print("min",min_val)
                while(sum_val>=target):
                    min_val = min(min_val,j-i+1)
                    sum_val = sum_val - nums[i]
                    i+=1
                    print("new sum", sum_val)
                j+=1
        
        if  min_val==100000:
            return 0
        else:
            return min_val
