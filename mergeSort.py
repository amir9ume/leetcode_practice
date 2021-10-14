class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.mergeSort(nums)
        print(nums)
        return nums[-k]            
    
    def merge(self,arr, leftArr, rightArr): 
          
        i=j=k=0
        while(i < len(leftArr) and j < len(rightArr)):
            if leftArr[i]<=rightArr[j]:
                arr[k]=leftArr[i]
                
                i+=1
            else:
                arr[k]=rightArr[j]
                
                j+=1
            k+=1
        
        while(i<len(leftArr)):
            arr[k]=leftArr[i]
            
            i+=1
            k+=1
        while(j<len(rightArr)):
            arr[k]=rightArr[j]
            
            j+=1
            k+=1
            
        
    def mergeSort(self,arr):
        if len(arr)>1:
            mid= len(arr)//2 

            left= arr[:mid]
            right= arr[mid:]

            self.mergeSort(left)
            self.mergeSort(right)
            self.merge(arr,left,right)
