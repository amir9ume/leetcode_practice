class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals)<=1:
            return intervals
        
        intervals.sort(key=lambda x : x[0])
        
        prev=intervals[0]
        
        i=1
        while(i<len(intervals)):
            curr= intervals[i]
            if prev[1]>= curr[0]:
                
                prev.extend(curr)
                
                prev.sort()
                new=[prev[0],prev[-1]] 
                intervals[i-1]=new
                intervals.pop(i)
                i-=1
            prev=intervals[i]
            i+=1    
            
        
        return intervals
