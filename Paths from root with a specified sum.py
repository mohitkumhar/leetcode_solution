# A Tree node
# struct Node
# {
#     int key;
#     struct Node *left, *right;
# };
class Solution:
    def printPaths(self, root, s):
        self.result = []

        def solve(node, curr_sum, curr_str):
            if not node:
                return None

            curr_sum += node.key
            curr_str.append(node.key)

            if curr_sum == s:
                self.result.append(curr_str[:])

            node.left = solve(node.left, curr_sum, curr_str)
            node.right = solve(node.right, curr_sum, curr_str)
            
            curr_str.pop()

            return node

        solve(root, 0, [])
        return self.result
