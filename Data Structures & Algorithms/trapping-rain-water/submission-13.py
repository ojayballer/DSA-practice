class Solution:
    def trap(self, height: List[int]) -> int:

        if not height :
            return 0
        
        l=0
        r=len(height)-1
        leftMax=height[l]
        RightMax=height[r]
        water=0
        while l < r :
                if leftMax <=RightMax:
                    l+=1
                    leftMax=max(leftMax,height[l])
                    if (min(leftMax,RightMax) - height[l])>0:
                         water+=min(leftMax,RightMax) - height[l]
        
                elif leftMax > RightMax:
                    r-=1
                    RightMax=max(RightMax,height[r])
                    if (min(leftMax,RightMax) - height[r])>0:
                         water+=min(leftMax,RightMax) - height[r]
                    
                   
        
        return water 
                
            


