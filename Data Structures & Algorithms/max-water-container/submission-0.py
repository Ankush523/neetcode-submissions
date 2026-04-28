class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        amt = min(heights[left],heights[right]) * (right-left)
        while(left<right):
            if(heights[left]<heights[right]):
                left+=1
            else:
                right-=1

            new_amt = min(heights[left],heights[right]) * (right-left)
            if(new_amt>amt):
                amt = new_amt
        return amt
