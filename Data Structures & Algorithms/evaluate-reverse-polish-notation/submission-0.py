class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def solve(int1, int2, operator):
            if operator == "+":
                return int1 + int2
            elif operator == "-":
                return int1 - int2
            elif operator == "*":
                return int1 * int2
            else:
                return int(int1 / int2)

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                int2 = stack.pop()
                int1 = stack.pop()
                stack.append(solve(int(int1), int(int2), token))

        return int(stack[0])