class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i :[] for i in range(n)}

        for a,b in edges :
            graph[a].append(b)
            graph[b].append(a)
        
        q=collections.deque()

        
        visit=set()
        def bfs(node):
              q.append(node)
              visit.add(node)
              while q :
                node = q.popleft()
                for nei in graph[node]:
                  if nei not in visit : 
                    visit.add(nei)
                    q.append(nei)

                    
                 
                  
        res=0
        for node in range(n):
            if node not in visit :
                bfs(node)   
                res+=1
        return res       
            
            
        

            
                
