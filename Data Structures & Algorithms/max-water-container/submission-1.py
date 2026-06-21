class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ##two pointer approach 
        l= 0 ; r = len(heights)-1 
        res =0 
        while l< r :
            area = min(heights[l],heights[r])*(r-l)
            res = max(res,area)

            # always move shorter side to find 2nd maximum height instead of moving both left and right pointers
            if heights[l] <= heights[r] :
                l+=1 
            else :
                r-=1

        return res 

       
              
        