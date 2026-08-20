class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for  s in tokens :
            if s  not in "+/-*" :
                stack.append(int(s))
            else :
                 if len(stack) >=2 :
                    a = stack.pop()
                    b=stack.pop()
                    if s == '+':
                       stack.append(b+a)
                    elif s== '-':
                       stack.append(b-a)
                    elif s== '/':
                        stack.append(int(b/a))
                    else :
                        stack.append(b*a)
        return stack.pop() if stack else 0 
            
