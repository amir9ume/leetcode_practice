class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums==None:
            return 0
        
        nums.sort()
        flag= True
        ctr=0
        size=len(nums)
        while(flag):
            out= self.binarySearch(nums,0,len(nums)-1,val)
            if out==-1:
                break
         
            nums.remove(nums[out])
            ctr+=1
      
        
    def binarySearch(self,nums,low,high,target):
        if low>high:
            return -1
        
        mid= (low+high)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            return self.binarySearch(nums,mid+1,high,target)
        if nums[mid]>target:
            return self.binarySearch(nums,low,mid-1,target)
        
