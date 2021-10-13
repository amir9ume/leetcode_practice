# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root==None:
            return False
        queue=[]
        queue.append(root)
        
        while(len(queue)>0):
            count=len(queue)
            
            temp=[]
            
            while(count>0):
                x= queue.pop(0)
                
                if x.left!=None:
                    temp.append(x.left.val)
                    queue.append(x.left)
                else:
                    temp.append('e')
                if x.right!=None:
                    temp.append(x.right.val)
                    queue.append(x.right)
                else:
                    temp.append('e')
                count-=1
            
            if temp!=temp[::-1]:
                return False
            
      
        return True
            
            
          
