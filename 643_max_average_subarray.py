#prepare array of cumulative sums
#diff= sums[k+ctr]- sums[ctr], gives subarray sums for length k
#get the highest diff, as the biggest subarray sum
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==1:
            return nums[0]
        
        sums=[0]
        for i in range(len(nums)):
            t= sums[i]+nums[i]
            sums.append(t)
        
        
        max= self.get_k_subarray_max_sum(sums,k)
       
    
        return max/k
    
    def get_k_subarray_max_sum(self,sums,k):
        ct=0
        max=-float("inf")
        while((ct+k) < len(sums)):
            diff= sums[k+ct]- sums[ct]
            if diff>=max:
                max=diff
            ct+=1    
        return max
