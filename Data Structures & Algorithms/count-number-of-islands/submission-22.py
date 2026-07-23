class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[-1,0],[1,0],[0,1],[0,-1]] 
        row=len(grid) ; column= len(grid[0])

       
        queue=collections.deque()
        def bfs(r,c):  
            queue.append((r,c))
            while queue : 
                r,c = queue.popleft()
                grid[r][c]='0'
                for dr,dc in directions :
                    vr,vc=r+dr ,c+dc 
                    if(vr<0 or vc<0 or vr >=row or vc >=column or grid[vr][vc]=='0'):
                        continue 
      
                    queue.append((vr,vc))
                    grid[vr][vc]= '0'
                
                
            

        count=0
        for r in range(row):
            for c in range(column):
                if grid[r][c] =='1':
                    bfs(r,c)
                    count+=1

        return count 
        

         
       





        
       