# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        self.result = '~'

        def backtrack(node, path):
            if not node:
                return
            path.append(chr(node.val + ord('a')))

            if not node.right and not node.left:
                leaf_to_root = ''.join(reversed(path))
                if leaf_to_root < self.result:
                    self.result = leaf_to_root
            
            backtrack(node.left, path)
            backtrack(node.right, path)
            path.pop()
        backtrack(root, [])

        return self.result
