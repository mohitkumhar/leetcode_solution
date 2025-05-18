# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        count = {}

        for res in result:
            if res in count:
                count[res] += 1
            else:
                count[res] = 1

        max_freq = max(count.values())
        mode = [num for num, freq in count.items() if freq == max_freq]

        return mode
