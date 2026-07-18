class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if  len(edges) != n -1 : #first exit condition 
            return False 

        graph = {i:[] for i in range(n)}
        
        q=collections.deque()
        for a,b in edges :
            graph[a].append(b)
            graph[b].append(a)
        
        #let's start bfs from 0,alternatively we can start from any node since this graph is not directed
        q.append(0)
        visit=set()
        while q :
            node= q.popleft()
            visit.add(node)
            
            for nei in graph[node]:
                if nei in visit :
                    continue 
                visit.add(nei)
                q.append(nei)
        
        for i in range(n):
            if i not in visit :
                return False 
        return True 





        