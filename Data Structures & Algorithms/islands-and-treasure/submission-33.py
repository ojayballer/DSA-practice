class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
       rows=len(grid) 
       columns=len(grid[0])
       directions = [[1,0],[-1,0],[0,1],[0,-1]]
       visit=[[False]*columns for i in range(rows)]
       q=deque()
       for r in range(rows):
         for c in range(columns):
            if grid[r][c] == 0:#multi-source bfs 
                q.append((r,c))
                visit[r][c]=True 
       dist=0
       while q :
            for i in range(len(q)):
              row,column = q.popleft()
              grid[row][column]=dist 
              for dr,dc in directions:
                  nr,nc=row+dr,column+dc
                  if(nr<0 or nc<0 or nr>=rows or nc>=columns or grid[nr][nc]== -1
                         or visit[nr][nc]):
                    continue 
                  visit[nr][nc]=True
                  q.append((nr,nc))
            dist+=1

       
                  
              