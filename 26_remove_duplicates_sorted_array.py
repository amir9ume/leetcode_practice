class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ctr=0
        r_ctr=0
        while(ctr<len(nums)):
            curr=nums[ctr]
            r_ctr=ctr+1
            while(r_ctr<len(nums)):
                ahead= nums[r_ctr]
                if curr==ahead:
                    nums.pop(r_ctr)
                else:
                    break
            ctr+=1
        
