class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes = {}
        indegree = [0] * numCourses

        for v, u in prerequisites:
            if not u in nodes:
                nodes[u] = []
            nodes[u].append(v)
            indegree[v] += 1

        queue = []
        result = []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.pop(0)
            result.append(curr)

            if curr in nodes:
                for nei in nodes[curr]:
                    indegree[nei]  -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        if len(result) != numCourses:
            return []
        return result
