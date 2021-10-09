class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        
        ar=[]
        for num in nums:
            ar.append(int(num))
        #print(ar)
        
        ar.sort()
        return str(ar[-k])
