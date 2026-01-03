class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        queue = [(startGene, 0)]
        visited = set()
        bank = set(bank)

        while queue:
            string, changes = queue.pop(0)

            if string == endGene:
                return changes

            string = list(string)

            for i in range(len(string)):
                char = string[i]

                string[i] = 'A'
                new_gene = ''.join(string)
                if new_gene not in visited and new_gene in bank:
                    queue.append((new_gene, changes + 1))
                    visited.add(new_gene)

                string[i] = 'C'
                new_gene = ''.join(string)
                if new_gene not in visited and new_gene in bank:
                    queue.append((new_gene, changes + 1))
                    visited.add(new_gene)

                string[i] = 'G'
                new_gene = ''.join(string)
                if new_gene not in visited and new_gene in bank:
                    queue.append((new_gene, changes + 1))
                    visited.add(new_gene)

                string[i] = 'T'
                new_gene = ''.join(string)
                if new_gene not in visited and new_gene in bank:
                    queue.append((new_gene, changes + 1))
                    visited.add(new_gene)

                string[i] = char

        return -1
