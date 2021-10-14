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
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        ar= self.getArrayForm(head)
        size=len(ar)
        if size<=1:
            return head
        
        if k>=size:
            k= k%size
        
        if k==0:
            return head
        moved= ar[-k:]
        reste= ar[:size-k]
        
        
        head= ListNode(moved[0])
        temp=head
        prev=head
        
        i=1
        while(i<len(moved)):
            temp= ListNode(moved[i])
            prev.next= temp
            prev= temp
            i+=1
        
        j=0
        while(j<len(reste)):
            temp= ListNode(reste[j])
            prev.next=temp
            prev= temp
            j+=1
        
        return head
