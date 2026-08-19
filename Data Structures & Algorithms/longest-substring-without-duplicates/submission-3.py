class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash =set()
        l=0 
        r=0
        max_seen=0
        while r < len(s):
            while s[r] in hash :
                hash.remove(s[l])
                l+=1
            max_seen=max(max_seen,r-l+1)
            hash.add(s[r])
            r+=1
            
            
        return max_seen
            #z|xyzx -> yzx
            
            


