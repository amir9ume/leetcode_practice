#uses dictionary to check if pair/tuple already exists or not
#though solution run time more, find way to optimize this

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        
        size=len(nums)
        
        k= abs(k)
        map={}
        i=0
        ct=0
        while(i<size):
            j=i+1
            while(j<size):
                diff= (nums[j]-nums[i])
                if diff>k:
                    break
                if diff==k:
                    t= (nums[i],nums[j])
                    if t not in map:
                        map[t]=True
                        ct+=1
                j+=1
            i+=1
        
        
        
        return ct
