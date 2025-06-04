# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        result = []
        queue1 = [root1]
        queue2 = [root2]

        while queue1:
            temp = []
            for node in queue1:
                if node:
                    result.append(node.val)
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            queue1 = temp

        while queue2:
            temp = []
            for node in queue2:
                if node:
                    result.append(node.val)
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            queue2 = temp

        return sorted(result)
