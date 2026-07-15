class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions =[[1,0],[-1,0],[0,1],[0,-1]]
        rows=len(grid) 
        columns =len(grid[0])
        q=deque()
        minutes=0
        fresh=0 
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]== 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
                    
        while fresh>0 and q :
            for i in range(len(q)):
                row,column = q.popleft()
                for dr,dc in directions :
                    nr,nc=row+dr,column+dc
                    if(nr<0 or nc<0 or nr>=rows or nc>=columns or grid[nr][nc]==0
                        or grid[nr][nc]==2 ): #fresh fruit 
                        continue 
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc))
            minutes+=1
            
        if fresh >0 :
            return -1 
        return minutes 
        

                   
                    
                    
                   

        