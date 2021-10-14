# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return False
        if head.next==None:
            return False
        
        if head.next.next==None:
            return False
        
        temp= head
        tempFast= head.next.next
        
        while(tempFast!=None and temp!=None):
            if temp==tempFast:
                return True
            temp=temp.next
            if tempFast.next!=None:
                tempFast= tempFast.next.next
            else:
                return False
        
        
        return False
