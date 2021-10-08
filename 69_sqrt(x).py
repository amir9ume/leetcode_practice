#solution using binary search
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        
        out= self.binarySearch( 0, x-1,x)
     
        return out
        
    def binarySearch(self, low, high,target):
        if low>=high:
           
            if low**2 <= target:
                return low
            if low**2 > target:
                return low-1
           
            return -1
        mid= (low+high)//2
        cand= mid**2
        
        if cand==target:
            return mid
        if cand>target:
            return self.binarySearch(low, mid-1,target)
        if cand< target:
            return self.binarySearch( mid+1,high,target)
        
        
