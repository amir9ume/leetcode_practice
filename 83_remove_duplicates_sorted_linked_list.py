class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        
        curr= head
        prev= curr
        map={}
        
        while(curr!=None):
            val= curr.val
          
            if val in map:
                prev.next=curr.next
                curr=prev
                
            else:
                map[curr.val]=True
            if curr.next==None:
                break
            prev= curr
            curr= curr.next
        return head
