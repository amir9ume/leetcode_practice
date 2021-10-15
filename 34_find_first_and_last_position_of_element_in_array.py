class Solution(object):
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x=self.binarySearch(nums,0,len(nums)-1,target)
        print(x)
        if x==-1:
            return [-1,-1]
        
        solns=[x]
        i=x+1
        while(i<len(nums)):
            if nums[i]==target:
                solns.append(i)    
            i+=1
        j=x-1
        while(j>=0):
            if nums[j]==target:
                solns.append(j)
            j-=1
        
        solns.sort()
        return [solns[0],solns[-1]]
        
    
    def binarySearch(self,ar,low,high,target):
        if low>high:
            return -1
        
        mid= (low+high)//2
        
        if ar[mid]==target:
            return mid
        if ar[mid]>target:
            return self.binarySearch(ar,low,mid-1,target)
        if ar[mid]<target:
            return self.binarySearch(ar,mid+1,high,target)
