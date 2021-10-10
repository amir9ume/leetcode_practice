class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctr=0
        stack=[]
        
        for c in s:
            if c not in stack:
                stack.append(c)
            else:
                stack.remove(c)
                ctr+=2
        if len(stack)>0:
            ctr+=1
        
        
        return ctr
