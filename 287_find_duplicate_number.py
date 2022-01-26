class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ar= nums.copy()
        ar.sort()
        temp= -1
        
        for a in ar:
            if a != temp:
                temp= a
            elif a== temp:
                return a
            
