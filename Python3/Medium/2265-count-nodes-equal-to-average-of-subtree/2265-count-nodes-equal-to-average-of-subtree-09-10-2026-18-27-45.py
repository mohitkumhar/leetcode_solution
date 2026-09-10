# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def solve(node):
            nonlocal count

            if not node:
                # sum, number of values
                return 0, 0

            leftSum, leftValues = solve(node.left)
            rightSum, rightValues = solve(node.right)

            currAvg = (leftSum + rightSum + node.val) // (leftValues + rightValues + 1)

            if currAvg == node.val:
                count += 1

            return leftSum + rightSum + node.val, leftValues + rightValues + 1

        count = 0

        solve(root)
        return count
