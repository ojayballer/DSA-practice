# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if not list1 and not list2 :
        return None 
      
      if list1 and not list2 :
        return list1 
      
      if list2 and not list1 :
        return list2 
      
      res =[]
      while list1 :
        res.append(list1.val)
        list1=list1.next
      
      while list2 :
        res.append(list2.val)
        list2=list2.next 
      
      res.sort()
      node=ListNode(res[0])
      current=node
      for r in res[1:] :
         current.next= ListNode(r)
         current=current.next 
      
      return node 



      
