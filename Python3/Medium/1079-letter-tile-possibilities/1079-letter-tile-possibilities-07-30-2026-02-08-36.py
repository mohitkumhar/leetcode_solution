class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def backtrack(i, currComb, used):
            nonlocal result
            result.add("".join(currComb))

            if i >= len(tiles):
                return

            for j in range(len(tiles)):
                if j in used:
                    continue

                currComb.append(tiles[j])
                used.add(j)

                backtrack(j, currComb, used)

                currComb.pop()
                used.remove(j)

        count = 0
        result = set()

        backtrack(0, [], set())

        return len(result) - 1
