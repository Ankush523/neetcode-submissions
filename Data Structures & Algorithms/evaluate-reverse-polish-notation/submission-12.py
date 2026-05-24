class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_operators = ["+", "*", "-", "/"]
        stack=[]
        result = 0
        for i in tokens:
            if i not in math_operators:
                stack.append(i)
            elif i in math_operators:
                expression = f"{stack[-2]} {i} {stack[-1]}"
                result = eval(expression)
                stack.pop()
                stack.pop()
                stack.append(int(result))
        return int(stack[0])