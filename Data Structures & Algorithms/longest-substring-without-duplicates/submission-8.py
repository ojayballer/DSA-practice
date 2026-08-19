class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0 
        hash=set()
        maxP=0
      
        while r < len(s):
            
            while s[r] in hash: 
                hash.remove(s[l])
                l+=1 
            maxP=max(maxP,r-l+1)
            hash.add(s[r])
            r+=1
        
        return maxP
        
#pwwkew  #l=p  #abc