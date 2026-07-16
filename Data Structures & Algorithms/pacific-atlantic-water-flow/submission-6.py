class Solution:
    def pacificAtlantic(self,heights: List[List[int]]) -> List[List[int]]:
        #pacific ocean 
        #atlantic ocean 
        directions=[[-1,0],[0,-1],[1,0],[0,1]] #top ,left,bottom,right
        rows,columns=len(heights),len(heights[0])
        

        pac=collections.deque()
        atl=collections.deque()
        visit_pac,visit_atl=set(),set()
        for r in range(rows):
            for c in range(columns):
                if r==0 or c == 0:
                    pac.append((r,c))
                if c==(columns-1) or r==(rows-1):
                    atl.append((r,c))

        def bfs(q,track):
            while q :
                    row,column = q.popleft()
                    track.add((row,column))
                    for r, c in directions :
                        nr,nc=r+row,c+column
                        if(nr<0 or nr>=rows or nc<0 or nc>=columns or (nr,nc)
                         in track or heights[nr][nc]<heights[row][column]):
                           continue
                        track.add((nr,nc))
                        q.append((nr,nc))
        #run bfs's
        bfs(pac,visit_pac) 
        bfs(atl,visit_atl)


        #result 
        res=[]
        for r in range(rows):
          for c in range(columns):
            if (r,c) in visit_pac and (r,c) in visit_atl:
                res.append([r,c])

        return res 
             

                          

                
        
            
        


                

