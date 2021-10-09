class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ar= [element for row in matrix for element in row]
        
        return self.binarySearch(ar,0,len(ar)-1,target)
        
    
    def binarySearch(self, nums, low, high, target):
        if low>high:
            return False
        
        mid= (low+high)//2
        
        if nums[mid]==target:
            return True
        if nums[mid]>target:
            return self.binarySearch(nums,low,mid-1,target)
        else:
            return self.binarySearch(nums,mid+1,high,target)
