# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def solve(root, sum):

            if not root:
                return sum

            sum = solve(root.right, sum)

            sum += root.val
            root.val = sum

            sum = solve(root.left, sum)

            return sum

        sum = 0
        solve(root, sum)

        return root
