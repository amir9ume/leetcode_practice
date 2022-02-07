class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums2)>len(nums1):
            t= nums1
            nums1=nums2
            nums2=t
        
        ar=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                ar.append(nums1[i])
        return ar
