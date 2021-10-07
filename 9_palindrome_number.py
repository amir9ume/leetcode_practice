#easy solution by reversing as a string
#will post different solutions soon 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        rep= str(x)
        if rep== rep[::-1]:
            return True
        else:
            return False
