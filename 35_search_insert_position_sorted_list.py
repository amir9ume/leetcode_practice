class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        out= self.binarySearch(nums,0,len(nums)-1,target)
        print(out)
        return out
    
    def binarySearch(self, nums, low, high, target):
        if low>=high:
            if nums[low]>target:
                return low
            elif nums[low]<target:
                    return low+1
        
        mid = (low+high)//2
        
        if nums[mid]==target:
            return mid
        
        if nums[mid]>target:
            return self.binarySearch(nums,low, mid-1,target)
        
        if nums[mid]<target:
            return self.binarySearch(nums,mid+1,high, target)
        
        
