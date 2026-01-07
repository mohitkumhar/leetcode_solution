class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        for i in range(len(graph)):

            if i not in colors:
                queue = [(i, 1)]
                colors[i] = 1

            while queue:
                node, curr_color = queue.pop(0)

                for neighbour in graph[node]:
                    if neighbour in colors:
                        if colors[neighbour] == curr_color:
                            return False

                    else:
                        queue.append((neighbour, -curr_color))
                        colors[neighbour] = -curr_color

        return True
