class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        #find the region where target is 
        top=len(matrix)-1
        bottom=0

        while bottom <= top :
            mid =(bottom + top)//2 

            if  matrix[mid][0] > target   :
                top=mid-1
            
            elif matrix[mid][-1] < target :
                bottom=mid+1

            else :
                break 

        
        new=matrix[mid]
        l=0
        r=len(new) -1 
        while l<=r :
             mid = (l+r)//2

             if new[mid] == target :
                return True 

             elif new[mid] > target :
                 r=mid-1

             else: # new[mid] < target :
                l=mid+1
        return False 
        