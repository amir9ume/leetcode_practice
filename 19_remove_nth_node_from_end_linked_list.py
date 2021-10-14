# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getArrayForm(self,head):
        
        if head==None:
            return []
        ar=[]
        temp=head
        while(temp!=None):
            ar.append(temp.val)
            temp=temp.next
        return ar
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head==None:
            return head
        
        ar= self.getArrayForm(head)
        size=len(ar)
        ar.pop(size-n)
        print(ar)
        if len(ar)<1:
            return None
        
        head=ListNode(ar[0])
        temp=head
        prev=head
        if len(ar)==1:
           
            head.next=None
            return head
        
        i=1
        while(i<len(ar)):
            temp= ListNode(ar[i])
            prev.next=temp
            prev=temp
            i+=1
        return head
