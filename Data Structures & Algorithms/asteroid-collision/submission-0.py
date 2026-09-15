class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        for asteroid in asteroids:
            while(len(s)>0 and s[-1]>0 and asteroid<0):
                if(s[-1] == abs(asteroid)):
                    s.pop()
                    break
                elif(s[-1]<abs(asteroid)):
                    s.pop()
                else:
                    break
            else:
                s.append(asteroid)      
        return s