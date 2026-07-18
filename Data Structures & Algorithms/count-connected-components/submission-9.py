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
              while q :
                node = q.popleft()
                visit.add(node) 
                for nei in graph[node]:
                  if nei in visit :
                    continue 
                  q.append(nei)
                  
        res=0
        for node in range(n):
            if node not in visit :
                bfs(node)   
                res+=1
        return res       
            
            
        

            
                
