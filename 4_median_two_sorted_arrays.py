class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ar= self.merge(nums1,nums2)
        
        size= len(ar)
        mid= size//2
        
        if size%2==0:
            return float(ar[mid]+ar[mid-1])/2.0
        else:
            return ar[mid]
        
    def merge(self,left,right):
        i=j=0
        ar=[]
        while(i<len(left) and j<len(right)):
            if left[i]<=right[j]:
                ar.append(left[i])
                i+=1
            else:
                ar.append(right[j])
                j+=1
        while(i<len(left)):
            ar.append(left[i])
            i+=1
        while(j<len(right)):
            ar.append(right[j])
            j+=1
        return ar
