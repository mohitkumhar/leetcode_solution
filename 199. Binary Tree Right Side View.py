# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        if not root:
            return result
        
        queue = [root]

        while queue:
            temp = []

            for i in range(len(queue)):
                node = queue[i]

                if node.left:
                    temp.append(node.left)
                
                if node.right:
                    temp.append(node.right)
                
            result.append(queue[-1].val)
            queue = temp
        
        return result
