# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete_set = set(to_delete)
        result = []

        def helper(node, is_root):
            if not node:
                return None

            root_delete = node.val in to_delete_set

            if not root_delete and is_root:
                result.append(node)
            
            node.left = helper(node.left, root_delete)
            node.right = helper(node.right, root_delete)

            return None if root_delete else node
        
        helper(root, True)
        return result

        