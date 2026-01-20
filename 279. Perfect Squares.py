class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1

        queue = [n]
        visited = {n}
        count = 1

        while queue:
            next_queue = []

            for node in queue:
                for square in squares:
                    temp = node - square

                    if temp == 0:
                        return count

                    if temp > 0 and temp not in visited:
                        next_queue.append(temp)
                        visited.add(temp)

            queue = next_queue
            count += 1
