class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        for t in tokens:
            if t.lstrip('-').isnumeric():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                match t:
                    case '+':
                        stack.append(a + b)
                    case '-':
                        stack.append(a - b)
                    case '*':
                        stack.append(a * b)
                    case '/':
                        stack.append(int(a / b))
                    case _:
                        raise Exception('wtf')
        return stack.pop()
