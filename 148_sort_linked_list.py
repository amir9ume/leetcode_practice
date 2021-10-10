# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ar=[]
        
        temp=head
        while(temp!=None):
            ar.append(temp.val)
            temp= temp.next
        
        ar.sort()
        temp=head
        for i in range(len(ar)):
            temp.val= ar[i]
            temp=temp.next
        return head
