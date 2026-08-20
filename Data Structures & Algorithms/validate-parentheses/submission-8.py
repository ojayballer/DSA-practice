class Solution:
    def isValid(self, s: str) -> bool:
        
        stack =[]
        closeToOpen= {')':'(','}':'{',']':'['}

        for i in range(0,len(s)):
                if s[i] in '[{(' :
                    stack.append(s[i])
                
                else :
                    if  stack and stack[-1] == closeToOpen[s[i]]:
                        stack.pop()
                        continue 
                    return False 
        
        return True if len(stack)==0 else False 