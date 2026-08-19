class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0 
        r=0 
        hm ={}
        maxV=0
        res =0 
        while  r < len(s):
            hm[s[r]] = hm.get(s[r],0) +1 
            maxV=max(hm[s[r]],maxV)

            while (r-l+1) - maxV >  k :
                hm[s[l]] -= 1 
                l+=1 

            res=max(res,r-l+1)
            r+=1 

        return res 

