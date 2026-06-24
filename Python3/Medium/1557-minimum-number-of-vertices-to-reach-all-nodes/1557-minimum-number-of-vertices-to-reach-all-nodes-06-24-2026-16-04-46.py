class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inorder = [0] * n

        for u, v in edges:
            inorder[v] += 1

        ans = []
        for i in range(n):
            if inorder[i] == 0:
                ans.append(i)
        return ans
