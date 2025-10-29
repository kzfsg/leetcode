# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# p and q will exist, no edge case
# node can be descendant of itself
# we need to search the entire tree

# DFS Recursive -> Bottom Up Approach
# Base case -> null node, return null, if we find p or q, return the node
# Recursive search -> search both left and right subtreees

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # base case null node
        if root is None:
            return None


        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        return left if left is not None else right
        