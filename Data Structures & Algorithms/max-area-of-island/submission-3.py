class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows=len(grid) 
        columns=len(grid[0])
        track=set()
        def dfs(r,c):

            if (r<0 or c<0 or r>=rows or c >=columns or grid[r][c]== 0 or
               (r,c) in track  ) :

                 return  0
            
            track.add((r,c)) #visited
            
            #return area as 1 if we dont find any other lands(1s)
            return 1+ (dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))

        #run dfs 
        area=0 
        for r in range(rows):
            for c in range(columns):
               if grid[r][c] == 1:
                 area= max(dfs(r,c),area)
        
        return area




            


        