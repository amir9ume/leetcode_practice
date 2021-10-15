class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        size=len(mat)
        ar = [e for row in mat for e in row]
        ar.sort()
        
        map={}
        for a in ar:
            if a not in map:
                map[a]=1
            else:
                map[a]+=1
        hold=[]
        for key in map:
            hold.append((map[key],key))
        hold.sort(key=lambda x: x[0])
      
        
        for h in hold:
            if h[0]==size:
                return h[1]
        return -1
