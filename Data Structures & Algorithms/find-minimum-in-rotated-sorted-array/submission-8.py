class Solution:
    def findMin(self, nums: List[int]) -> int: #lower-bound method 
       left =0 
       right =len(nums)-1 

       while (left< right): #time:O(log(n)),space=O(1)
         
         mid=(left+right)//2 

         if nums[mid] <nums[right]: #if 
            right =mid 
         else : #nums[mid]>=nums[left]
            left=mid+1
            
       return nums[left]
        