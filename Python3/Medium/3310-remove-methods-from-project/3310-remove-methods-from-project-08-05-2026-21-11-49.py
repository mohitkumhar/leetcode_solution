class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:

        matrix = {i: [] for i in range(n)}

        for invocation in invocations:
            matrix[invocation[0]].append(invocation[1])


        queue = [k]
        visited1 = {k}

        while queue:
            node = queue.pop(0)

            for nei in matrix[node]:
                if nei not in visited1:
                    visited1.add(nei)
                    queue.append(nei)

        visited2 = set()
        result = []

        for node in range(n):
            if node in visited1:
                continue

            if node in visited2:
                continue

            queue = [node]
            visited2.add(node)

            while queue:
                currNode = queue.pop(0)
                result.append(currNode)

                for nei in matrix.get(currNode):
                    if nei not in visited2:
                        visited2.add(nei)
                        queue.append(nei)

        for u, v in invocations:
            if u not in visited1 and v in visited1:
                return list(range(n))

        return result
