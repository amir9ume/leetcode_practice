# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        if root==None:
            return None
        sums=[]
        stack= [(root, root.val)]
        while(len(stack)>0):
            x, currSum= stack.pop()
            
            if x.left==None and x.right==None:
                if currSum == targetSum:
                    return True
                sums.append(currSum)
            
            if x.left!=None:
                stack.append((x.left, currSum+x.left.val))
                
            if x.right!=None:
                stack.append((x.right, currSum+x.right.val))
        print(sums)
        
        return False
