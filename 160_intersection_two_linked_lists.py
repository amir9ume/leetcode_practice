# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        t1=headA
        t2=headB
        map1={}
        
        while(t1!=None):
            map1[t1]=True
            t1= t1.next
        
        while(t2!=None):
            if t2 in map1:
                return t2
            t2= t2.next
        
        return None
            
