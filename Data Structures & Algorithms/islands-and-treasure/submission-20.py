class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        rows,columns=len(grid) ,len(grid[0])
        INF=2147483647

        def bfs(r,c):
            q=deque([(r,c)])
            
            visit=[[False]*columns for _ in range(rows)]
            steps=0
            visit[r][c]= True 

            while q :
              for j in range(len(q)):
                row,col=q.popleft()
                if grid[row][col] == 0:
                    return steps
                for dr,dc in directions :
                   a,b=row+dr ,col+dc
                   if(a<0  or b <0 or a>=rows or b >= columns or grid[a][b] == -1 or visit[a][b]) :
                       continue 
                   visit[a][b] =True 
                   q.append((a,b))
              steps+=1
            return INF 
           
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]== INF :
                   grid[r][c] = bfs(r,c )
           


                

            
            
            
        
        