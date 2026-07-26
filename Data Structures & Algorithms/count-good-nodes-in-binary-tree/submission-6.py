# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    

        q=collections.deque()
        q.append([root,root.val])
        
        if not root :
            return []
        
        good=0
        maxVal=root.val
        while q :
                node,maxVal=q.popleft()

                if node.val >= maxVal :
                    good+=1

                maxVal=max(node.val,maxVal)


                if node.left :
                   q.append([node.left,maxVal])
                   
                if node.right :
                    q.append([node.right,maxVal])

        
                   
        return good 