class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        dist=[ ((a -x),a) for a in arr]
        dist.sort(key= lambda x: abs(x[0]) or x[0])
        
        vals=[0 for i in range(k)]
        for i in range(k):
            vals[i]= dist[i][1]
        vals.sort()
        return vals
