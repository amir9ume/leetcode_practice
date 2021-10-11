class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_map={}
        for c in s:
            if c not in s_map:
                s_map[c]=1
            else:
                s_map[c]+=1
        
        t_map={}
        for c in t:
            if c not in t_map:
                t_map[c]=1
            else:
                t_map[c]+=1
        
        for key in t_map:
            if key not in s_map:
                return key
            if t_map[key]!=s_map[key]:
                return key
        
