class Solution:
    def isHappy(self, n: int) -> bool:
        slow =n
        fast = self.sumofSquares(n)

        while slow != fast :
            slow= self.sumofSquares(slow)
            fast = self.sumofSquares(fast)
            fast=self.sumofSquares(fast)  #terminate if slow == fast ,which means a cycle has been detected 

        if fast == 1 :
                return True
        
        return False 
        
    def sumofSquares(self,n) :
        output = 0 
        while n :
            digit=n % 10 
            digit = digit** 2  ##101 %10 =10 rem 1 ,10 % 10 =1 rem 0 ,1%10 = 0 rem 1,extract last digit 
            output += digit 
            n = n //10  #remove the digit 

        return output 



    

