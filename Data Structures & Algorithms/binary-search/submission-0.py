class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' for python , mid=(right-left)//2 but
        for other languages like C++ we use
                    mid = left + (right -left)//2
                    to avoid overflow errors,so
                    it is safer to use           
                  mid = left + (right -left)//2
        '''

        

        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right -left)//2

            if nums[mid]==target:
                return mid

            elif nums[mid] <target:
                left=mid+1
            
            elif nums[mid] >target:
                right=mid-1
        return -1










