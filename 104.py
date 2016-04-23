#104 maximum-depth-of-binary-tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0;
        lheight=self.maxDepth(root.left)
        rheight=self.maxDepth(root.right)
        return max(lheight,rheight)+1
