class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_sp = []
        for i in range(0, len(position)):
            pos_sp.append([position[i],speed[i]])
        pos_sp.sort(reverse=True) 

        s=[]
        for pos_sp_car in pos_sp:
            arr_t = (target-pos_sp_car[0])/pos_sp_car[1]
            while(len(s)>0 and arr_t<=s[-1]):
                break
            else:
                s.append(arr_t)
        return len(s)