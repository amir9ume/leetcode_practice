class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prod=1
        i=1
        for num in nums:
            if num==0:
                return 0
            elif num>0:
                prod=prod *1
            else:
                prod=prod*-1  
            i+=1
            
        return prod
