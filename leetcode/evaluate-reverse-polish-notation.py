class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in operators:
                secondNum = stack.pop()
                firstNum = stack.pop()
                val = self.calculate(firstNum, secondNum, token)
                stack.append(val)
            else:
                stack.append(token)
        return int(stack[0])

    def calculate(self, a, b, operator):
        if operator == "+":
            return int(a) + int(b)
        elif operator == "-":
            return int(a) - int(b)
        elif operator == "*":
            return int(a) * int(b)
        elif operator == "/":
            return int(int(a) / int(b))
        else:
            raise Exception("invalid operator")
