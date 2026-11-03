class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

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
                newGene = "".join(string)
                if newGene not in visited and newGene in bank:
                    queue.append((newGene, dist + 1))
                    visited.add(newGene)

                string[i] = "C"
                newGene = "".join(string)
                if newGene not in visited and newGene in bank:
                    queue.append((newGene, dist + 1))
                    visited.add(newGene)

                string[i] = "G"
                newGene = "".join(string)
                if newGene not in visited and newGene in bank:
                    queue.append((newGene, dist + 1))
                    visited.add(newGene)

                string[i] = "T"
                newGene = "".join(string)
                if newGene not in visited and newGene in bank:
                    queue.append((newGene, dist + 1))
                    visited.add(newGene)
                
                string[i] = char

        return -1
