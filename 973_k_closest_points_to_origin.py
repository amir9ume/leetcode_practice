class Solution(object):
    def distance(self,point):
        x= point[0]
        y= point[1]
        return (x**2 + y**2)#**(0.5)
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        self.mergeSort(points)
        #print(points)
        return points[:k]
    
    def mergeSort(self, ar):
        if len(ar)>1:
            mid= len(ar)//2
            left= ar[:mid]
            right= ar[mid:]
            
            self.mergeSort(left)
            self.mergeSort(right)
            self.merge(ar,left,right)
    
    def merge(self,ar, left,right):
        i=j=k=0
        while(i<len(left) and j<len(right)):
            if self.distance(left[i])<=self.distance(right[j]):
                ar[k]=left[i]
                i+=1
            else:
                ar[k]=right[j]
                j+=1
            k+=1
        
        while(i<len(left)):
            ar[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            ar[k]=right[j]
            j+=1
            k+=1
            
            
        
        
        
    
