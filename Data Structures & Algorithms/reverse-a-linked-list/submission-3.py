# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None 
        res=[]
        while head :
            res.append(head.val)
            head=head.next 
        
        res=res[::-1]
        
        node=ListNode(res[0])
        current=node
        for head in res[1:]:
            current.next=ListNode(head)
            current=current.next
        
        return node
        
