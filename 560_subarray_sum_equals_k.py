class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
       
        cumulative=[0]
        
        sum=0
        for num in nums:
            sum+=num
            cumulative.append(sum)
       
        
        ctr=0
        count=0
        while( ctr < len(cumulative)):
            j= 1
          
            while(j + ctr <len(cumulative)):
                diff= cumulative[j+ctr] - cumulative[ctr]
                
                if diff==k:
                    count+=1   
                j+=1
        
            ctr+=1
        return count
