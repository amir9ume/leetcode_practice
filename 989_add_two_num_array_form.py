class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        sum = 0
        size= len(num)
        for i in range(size):
            sum = sum + num[i] * (10**(size- i -1))
        sum= sum + k
     
        
        l=[]
        if sum==0:
            return [0]
        while(sum>0):
            remainder= sum %10
            sum = sum / 10
            l.append(remainder)
    
        return l[::-1]
