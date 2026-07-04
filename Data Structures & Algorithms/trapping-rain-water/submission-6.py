class Solution:
    def trap(self, height: List[int]) -> int:
         if not height :
            return 0 
         l=0 
         r=len(height)-1 
         leftMax=height[l]
         RightMax=height[r]
         
         res=0 
         while l<r:
            if leftMax < RightMax :
                l+=1
                leftMax=max(leftMax,height[l])
                res+=leftMax-height[l]

            else :
                r-=1
                RightMax=max(RightMax,height[r])
                res+=RightMax-height[r]
            
         return res 




