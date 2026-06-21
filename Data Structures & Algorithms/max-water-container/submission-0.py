class Solution:
    def maxArea(self, heights: List[int]) -> int:
        stop=len(heights)
        res=0
        for i in range(stop):
            for j in range(i+1,stop) :
                res = max(res,min(heights[i],heights[j])*(j-i))
        
        return res
              
        