
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

      if not node :
         return None 
        
      hash ={}
      q=collections.deque()
      hash[node] =Node(node.val)
      q.append(node)

      while q :
         curr = q.popleft()
         for nei in curr.neighbors:
            if nei not in hash :
                hash[nei]=Node(nei.val)
                q.append(nei)
            hash[curr].neighbors.append(hash[nei])

      return hash[node]
