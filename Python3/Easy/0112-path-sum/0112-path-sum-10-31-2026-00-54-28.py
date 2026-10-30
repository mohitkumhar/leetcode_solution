# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]

        while stack:
            node, currSum = stack.pop()

            currSum += node.val

            if not node.left and not node.right:
                if currSum == targetSum:
                    return True

            if node.left:
                stack.append((node.left, currSum))
            if node.right:
                stack.append((node.right, currSum))

        return False
