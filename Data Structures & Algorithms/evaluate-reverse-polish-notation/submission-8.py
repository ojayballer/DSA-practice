class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens :
            if token == '+' or token =='-' or token == '*'or token =='/':
                if stack and len(stack) >=2 :
                    res=stack.pop()
                    res1=stack.pop()

                    if token == '+':
                        a=int(res1) + int(res)
                        stack.append(a)
                    elif token == '-':
                        a=int(res1) - int(res)
                        stack.append(a)
                    
                    elif token == '*':
                        a=int(res1)*int(res)
                        stack.append(a)
                    elif token == '/':
                        a= int(int(res1) / int(res))##division always truncates toward 0 .
                        stack.append(a)

            else :
                stack.append(int(token)) # incase of a single input 
        return stack.pop()