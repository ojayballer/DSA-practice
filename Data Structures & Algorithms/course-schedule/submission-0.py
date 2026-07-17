class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #//build DAG 
        indegree=[0]*numCourses
        graph={i :[] for i in range(numCourses)} # [0:{},1:{},..]
        for course,prereq in prerequisites:
            indegree[course]+=1 #//how many prerequisites does this course need to be taken ?
            graph[prereq].append(course)#the courses a prereq unlocks 

        q=collections.deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        complete=0
        while q :
            node =q.popleft()
            complete+=1
            
            for nei in graph[node]:
                indegree[nei]-=1

                if indegree[nei] == 0:
                    q.append(nei)
        
        return complete == numCourses
        
        

