# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        results = []

        while queue:
            temp = []
            values = []

            for node in queue:
                values.append(node.val)

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            results.append(values)
            queue = temp
        
        index = 1
        for result in results:
            if index % 2 == 0:
                result.reverse()
            index += 1

        return results
