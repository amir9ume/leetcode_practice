# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root==None:
            return None
        
        
        stack=[(root, str(root.val))]
        
        sum=0
        while(len(stack)>0):
            x, path = stack.pop()
            
            if x.left==None and x.right==None:
                sum+=int(path)

            if x.left!=None:
                stack.append((root.left, path+str(root.left.val)))
            
            if x.right!=None:
                stack.append((root.right, path+str(root.right.val)))
          
        
        return sum
                
