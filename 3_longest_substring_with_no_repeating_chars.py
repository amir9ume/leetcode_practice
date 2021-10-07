class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1:
            return 0
        if len(s)==1:
            return 1
        
        history={}
        l_ctr=0
        r_ctr=l_ctr
        
        max_diff=0
        
        while(l_ctr<len(s)):
            if r_ctr==len(s):
                r_ctr=l_ctr
            
            char= s[r_ctr]
            if char not in history:
                history[char]=True
                r_ctr+=1
                diff= r_ctr - l_ctr
                
                if diff> max_diff:
                    max_diff= diff
            else:
                history.clear()
                l_ctr+=1
                r_ctr= l_ctr
            
        return max_diff
        
