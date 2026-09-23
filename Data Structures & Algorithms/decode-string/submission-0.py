class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for i in range(0, len(s)):
            if(s[i] != ']'):
                st.append(s[i])
            else:
                popped_nums = []
                popped_items = []
                while(len(st)>0 and st[-1]!='['):
                    popped_items.append(st.pop())
                st.pop()
                while(len(st)>0 and st[-1].isdigit()):
                    popped_nums.append(st.pop())
                popped_nums.reverse()
                k = int("".join(map(str, popped_nums)))
                popped_items.reverse()
                str_to_pass = str("".join(map(str, popped_items)))
                x = k * str_to_pass
                for j in x:
                    st.append(j)
        return "".join(st)