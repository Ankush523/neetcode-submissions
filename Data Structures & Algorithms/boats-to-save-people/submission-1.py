class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c=0
        left = 0
        right= len(people)-1
        while(left<=right):
            if (people[left] + people[right] <= limit):
                c+=1
                left +=1
                right -=1
            else:
                c+=1
                right -=1
        
        return c
