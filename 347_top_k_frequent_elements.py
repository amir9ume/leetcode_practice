class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts={}
        
        for num in nums:
            if num not in counts:
                counts[num]=1
            else:
                counts[num]+=1
        
        hold=[]
        for key in counts:
            hold.append((counts[key],key))
            
        hold.sort(key=lambda x: x[0])
        hold= hold[::-1][:k]
        
        solns= []
        for h in hold:
            solns.append(h[1])
        
        return solns
