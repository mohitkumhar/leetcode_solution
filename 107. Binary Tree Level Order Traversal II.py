# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            temp_nodes = []
            level_val = []

            for node in queue:
                level_val.append(node.val)

                if node.left:
                    temp_nodes.append(node.left)
                
                if node.right:
                    temp_nodes.append(node.right)
            
            result.append(level_val)
            queue = temp_nodes
        
        return result[::-1]

            
        