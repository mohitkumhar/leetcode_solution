class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        matrix = {i: [] for i in range(n)}

        for i in range(n):
            if parent[i] == -1:
                continue
            matrix[parent[i]].append(i)

        print(matrix)

        def dfs(node):
            char = ord(s[node]) - ord("a")

            nearestAncestor = lastSeen[char]
            if nearestAncestor != -1:
                newParent[node] = nearestAncestor

            prev = lastSeen[char]
            lastSeen[char] = node

            for child in matrix[node]:
                dfs(child)
            lastSeen[char] = prev

        lastSeen = [-1] * 26
        newParent = parent[:]

        dfs(0)

        newMatrix = {i: [] for i in range(n)}

        for i in range(1, n):
            newMatrix[newParent[i]].append(i)

        def calculate(node):
            for child in newMatrix[node]:
                calculate(child)
                result[node] += result[child]

        result = [1] * n
        calculate(0)
        return result
