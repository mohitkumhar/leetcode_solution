class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        matrix = {i:[] for i in range(n)}

        for u, v in edges:
            matrix[u].append(v)
            matrix[v].append(u)

        def dfs(node, parent):
            freq = {}
            freq[labels[node]] = freq.get(labels[node], 0) + 1

            for child in matrix.get(node, []):
                if child == parent:
                    continue
                
                label_elements_in_child = dfs(child, node)

                for key, value in label_elements_in_child.items():
                    freq[key] = freq.get(key, 0) + value

                
            ans[node] += freq[labels[node]]
            return freq
        
        ans = [0] * n
        dfs(0, -1)

        return ans