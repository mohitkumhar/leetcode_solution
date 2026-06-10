class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        child_to_parent = {}
        matrix = {}

        # checking every child has only one parent
        for i in range(n):
            if leftChild[i] != -1:
                if leftChild[i] in child_to_parent:
                    return False
                child_to_parent[leftChild[i]] = i
                if i not in matrix:
                    matrix[i] = []
                matrix[i].append(leftChild[i])

            if rightChild[i] != -1:
                if rightChild[i] in child_to_parent:
                    return False
                child_to_parent[rightChild[i]] = i
                if i not in matrix:
                    matrix[i] = []
                matrix[i].append(rightChild[i])

        # checking only one root node exists
        root = -1
        for i in range(n):
            if i not in child_to_parent:
                if root != -1:
                    return False
                root = i

        if root == -1:
            return False

        # check if n node exists
        queue = [root]
        count = 1
        visited = {root}

        while queue:
            nodes = queue.pop(0)
            for neighbor in matrix.get(nodes, []):
                if neighbor not in visited:
                    count += 1
                    visited.add(neighbor)
                    queue.append(neighbor)

        return count == n
