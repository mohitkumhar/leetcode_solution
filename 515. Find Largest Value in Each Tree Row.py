# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = [root]

        while queue:
            temp = []
            max_count = []
            for node in queue:
                if node:
                    max_count.append(node.val)
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)

            if max_count:
                result.append(max(max_count))
            queue = temp

        return result
        