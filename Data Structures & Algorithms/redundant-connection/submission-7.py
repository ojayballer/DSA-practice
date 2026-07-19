class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(1,len(edges)+1)}

        def bfs(a,b,graph):
            visit=set()
            q=collections.deque()
            q.append(a)
            visit.add(a)
            while q :
              node=q.popleft()
              if node == b :
                return True 
              for nei in graph[node] :
                  if nei not in visit :
                    visit.add(nei)
                    q.append(nei)
            return False 
        
        
        result=[]
        for a ,b in edges :
            if bfs(a,b,graph) :
                result.append([a,b])
            graph[a].append(b)
            graph[b].append(a)
        return edges[-1] if len(result)>1 else result[0]



