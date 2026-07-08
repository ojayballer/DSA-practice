class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0 
        bot=len(matrix)-1

        while top <= bot :
            row=(top+bot)//2

            if target >matrix[row][-1]:
               top=row+1
            
            elif target < matrix[row][0]:
                bot=row-1

            else :
                break

        if not top<=bot : #early exit condition
            return False

        l,r=0,len(matrix[row])-1 

        while l<=r :
            mid=(l+r)//2 

            if target>matrix[row][mid] :
                l+=1

            elif target<matrix[row][mid] :
                r-=1

            else :
                return True 
        return False


            


        



        