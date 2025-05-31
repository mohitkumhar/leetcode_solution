# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        result = []
        queue = [cloned]

        while queue:
            temp = []
            for node in queue:
                if node.val == target.val:
                    return node

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            queue = temp
