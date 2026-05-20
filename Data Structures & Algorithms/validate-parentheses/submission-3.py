class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack=[]
        for i in s:
            if i not in bracket_map:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top_element = stack.pop()
                    if bracket_map[i] != top_element:
                        return False
        return len(stack) == 0