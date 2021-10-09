class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr=[ e for row in matrix for e in row]
        #print(arr)
        arr.sort()
        return arr[k-1]
