from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque()
        queue.append((startGene, 0))
        visited = set()
        bank = set(bank)

        while queue:
            string, dist = queue.popleft()

            if string == endGene:
                return dist

            string = list(string)

            for i in range(len(string)):
                char = string[i]

                string[i] = "A"
                new_gene = ''.join(string)
                if new_gene not in visited and new_gene in bank:
                    queue.append((new_gene, dist + 1))
                    visited.add(new_gene)
                
                string[i] = "C"
                new_gene = ''.join(string)
                if new_gene not in visited and new_gene in bank:
                    queue.append((new_gene, dist + 1))
                    visited.add(new_gene)
                
                string[i] = "G"
                new_gene = ''.join(string)
                if new_gene not in visited and new_gene in bank:
                    queue.append((new_gene, dist + 1))
                    visited.add(new_gene)

                string[i] = "T"
                new_gene = ''.join(string)
                if new_gene not in visited and new_gene in bank:
                    queue.append((new_gene, dist + 1))
                    visited.add(new_gene)
                
                string[i] = char
        
        return -1





