# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[]
        while head :
            nodes.append(head)
            head=head.next 
        count=len(nodes) #[1,2]
        nodes.pop(count-n)
        if not nodes  :
            return None 

        newhead=nodes[0]
        curr=newhead
        for node in nodes[1:]:
            curr.next=node 
            curr=node
        
        curr.next=None
        
        return newhead 
            

        
        

        