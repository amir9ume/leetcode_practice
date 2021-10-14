# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getArray(self,head):
        ar=[]
        if head==None:
            return []
        temp=head
        while(temp!=None):
            ar.append(temp.val)
            temp=temp.next
        return ar
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arLists=[]
        for l in lists:
            x= self.getArray(l)
            arLists.extend(x)
        
        arLists.sort()
        print(arLists)
        if arLists==None:
            return None
        if len(arLists)<1:
            return None
        head=ListNode(arLists[0])
        prev=head
        
        for i in range(1,len(arLists)):
            temp= ListNode(arLists[i])
            prev.next=temp
            prev= temp
        return head
        
        
