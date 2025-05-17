# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        result = []

        while queue:
            temp = []
            for node in queue:
                result.append(node.val)
                if node.left:
                    temp.append(node.left)                
                if node.right:
                    temp.append(node.right)
            queue = temp
        final = sorted(set(result))

        if len(final) >= 2:
            return final[1]
        else:
            return -1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        result = []

        while queue:
            temp = []
            for node in queue:
                result.append(node.val)
                if node.left:
                    temp.append(node.left)                
                if node.right:
                    temp.append(node.right)
            queue = temp
        final = sorted(set(result))

        if len(final) >= 2:
            return final[1]
        else:
            return -1
