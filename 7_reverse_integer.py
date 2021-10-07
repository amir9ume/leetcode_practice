class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print(x)
        neg= False
        if x < 0:
            neg= True
            x = x*-1
        
        rep= str(x)[::-1]
        
        
        out= int(rep)
        if out>= (2**31):
            return 0
        if neg:
            return out * -1
        else:
            return out
