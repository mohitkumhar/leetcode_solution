# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def bst_to_arr(root, arr):
            if root:
                bst_to_arr(root.left, arr)
                arr.append(root.val)
                bst_to_arr(root.right, arr)

        def solve(start, end, arr):

            if start > end:
                return None

            mid = start + (end - start) // 2

            node = TreeNode(arr[mid])
            node.left = solve(start, mid - 1, arr)
            node.right = solve(mid + 1, end, arr)

            return node

        bst_arr = []
        bst_to_arr(root, bst_arr)

        start = 0
        end = len(bst_arr) - 1
        return solve(start, end, bst_arr)
