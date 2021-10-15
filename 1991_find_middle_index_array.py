class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        for i in range(len(nums)):
            c= self.binaryCheck(nums,i)
            if c==i:
                return c
            
        return -1
            
    def binaryCheck(self,ar, mid):
        left= ar[:mid]
        
        right=ar[mid+1:]
        
        i=j=0
        
        sumLeft=0
        while(i<len(left)):
            sumLeft+=left[i]
            i+=1
        
        j=0
        sumRight=0
        while(j<len(right)):
            sumRight+=right[j]
            j+=1
            
        if sumLeft==sumRight:
            return mid
        else:
            return -1
            
