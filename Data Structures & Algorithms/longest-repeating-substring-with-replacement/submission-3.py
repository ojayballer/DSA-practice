class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0 
        r=0 
        res=0 
        count ={}
        var=0
        while r < len(s):
            count[s[r]]= count.get(s[r],0) +1
            res= max(res,count[s[r]])

            while (r-l+1) - res > k:
                count[s[l]]-=1 
                l+=1

            var = max(var,r-l+1)
            r+=1
        return var

            