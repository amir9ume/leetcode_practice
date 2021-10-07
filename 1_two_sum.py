class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<1:
            return None
        
        remainder={}
        
        nums_remainder= [ target -n for n in nums]
        for i, rem in enumerate(nums_remainder):
            remainder[rem] = i   
    
        soln=[]
        for i,num in enumerate(nums):
            if num in remainder:
                x= remainder[num]
                if x!=i:
                    soln.append(i)
                    soln.append(x)
                    return soln
