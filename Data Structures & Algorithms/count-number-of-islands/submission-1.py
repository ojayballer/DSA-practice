class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #row controls up/down,column controls left/right
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # down,up ,right,left 
        
        rows =len(grid) ; columns=len(grid[0])
        island_counter=0 

        def dfs(r,c) :
            #if out of bounds or we find water then exit 
            if(r<0 or c<0 or r>=rows or c>=columns or grid[r][c] == '0'):
                 return 
            
            grid[r][c] = '0' #save memory,we dont have to process this again

            for dr,dc in directions :
                dfs(r+dr,c+dc) #we move with this and get the next position
            
        #run dfs 
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    dfs(r,c)
                    island_counter+=1


        return island_counter   
        




        