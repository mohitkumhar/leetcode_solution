class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        seen = set()
        count = 0
        matrix = {}

        for i in range(len(isConnected)):
            matrix[i] = []
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    matrix[i].append(j)

        def dfs(root):
            for node in matrix[root]:
                if node not in seen:
                    seen.add(node)
                    dfs(node)

        for node in matrix:
            if node not in seen:
                seen.add(node)
                dfs(node)
                count += 1

        return count
