class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        map={}
        
        for c in s:
            if c not in map:
                map[c]=1
            else:
                map[c]+=1
        
        for i in range(len(s)):
            c= s[i]
            if map[c]==1:
                return i
        
        return -1
        
