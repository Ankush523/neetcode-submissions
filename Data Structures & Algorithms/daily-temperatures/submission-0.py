class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        result = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            while (len(s)>0 and temperatures[i] > temperatures[s[-1]]):
                popped_index = s.pop()
                result[popped_index] = i - popped_index
            s.append(i)
        return result