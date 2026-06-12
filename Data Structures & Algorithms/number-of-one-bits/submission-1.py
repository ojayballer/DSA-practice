class Solution:
    def hammingWeight(self, n: int) -> int:
        #n=str(n) apparently python would convert the binary num to dec
        n =bin(n) # i have to explicitly ask it to leave it as a binary number 
        count=0
        for i in n :
            if i == '1' :
                count+=1

        return  count