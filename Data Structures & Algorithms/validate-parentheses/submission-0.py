class Solution:
    def isValid(self, s: str) -> bool:


       stack =[]
       closeToOpen ={')':'(','}':'{',']':'['}
       for i in s : #go through each element in the string 
        if i in closeToOpen: # if the elment is in closetopen, only closing elemnts work here 
          if stack and stack[-1]==closeToOpen[i] : # if the stack is not empty and the last eelemnt of the stack is equal to closetoopen[i]
             stack.pop() # removes the last elemnt 
          else :
            return False 
        else :
            stack.append(i) # append only openeing eleemnts 
       return len(stack) == 0 # return True or False if the stack is empty      


       '''   #brute force approach
        while '()' in s or '{}' in s or '[]' in s :
            #s.replace returns the original string into s if the substring is not present ,so it doesn't crash
            s=s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')
        
        #if s is empty ,then we have found a valid substring,if  s is not empty,then something did not have a matching pair

        return s == '' # retruns True or False '''
  
          



