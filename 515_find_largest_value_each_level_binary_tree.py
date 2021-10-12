# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root==None:
            return None
        
        solns=[]
        queue=[]
        queue.append(root)
        while(len(queue)>0):
            count= len(queue)
            
            maxVal= - float('inf')
            while(count>0):
                x= queue.pop(0)
                if x.val>maxVal:
                    maxVal= x.val
                
                if x.left!=None:
                    queue.append(x.left)
                if x.right!=None:
                    queue.append(x.right)
                count-=1
            solns.append(maxVal)    
        return solns
        
