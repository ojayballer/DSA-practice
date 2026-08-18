class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights) -1 
        res=0
        while l < r :
            m=(r-l) * min(heights[l],heights[r])
            if heights[r] >= heights[l]:
                l+=1
            elif heights[l]> heights[r]:
                r-=1 
            
            res=max(m,res)
        return res 
        