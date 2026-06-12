class Solution:
    def isHappy(self, n: int) -> bool:
        hash = set()

        while n not in hash :
            hash.add(n)
            n = self.sumofSquares(n)
            if n == 1 :
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



    

