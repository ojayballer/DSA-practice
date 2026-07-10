class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows=len(grid) 
        columns=len(grid[0])
        #track=set() #now we can optimize space to O(1) ,we have to remove the tracker 
        def dfs(r,c):

            if (r<0 or c<0 or r>=rows or c >=columns or grid[r][c]== 0 ):

                return  0
            
            #track.add((r,c)) #visited
            grid[r][c]=0 # change to O instead so we don't revisit this node again
            
            #return area as 1 if we dont find any other lands(1s)
            return 1+ (dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))

        #run dfs 
        area=0 
        for r in range(rows):
            for c in range(columns):
               if grid[r][c] == 1:
                 area= max(dfs(r,c),area)
        
        return area




            


        