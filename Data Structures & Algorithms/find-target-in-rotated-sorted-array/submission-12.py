class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1 

        while left<=right:
           mid=(left+right)//2

           if nums[mid] == target : #base condition
                 return mid 
            
           if nums[left]<=nums[mid]:
                if target>nums[mid] or target <nums[left]:
                    left=mid+1
                else :
                    right=mid-1

           elif nums[right] >nums[mid]:
                 if  target < nums[mid] or target > nums[right]:
                    right=mid-1

                 else:
                    left=mid+1
            
        return -1 #time:O(log(n)),space:O(1)
