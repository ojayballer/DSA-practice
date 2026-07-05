class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res=0
        for char in charSet : # O(1) look-up
            l=0
            count = 0 

            for r in range(len(s)): #O(n)
                if  s[r]==char :
                    count +=1 
                
                while (r-l+1)-count >k :#invalid window , O(m)
                    if s[l] == char :
                        count-=1 
                    l+=1
                
                res = max(res,r-l+1)
        return res 

        #time :O(n*m)
        #space :0(1)



        