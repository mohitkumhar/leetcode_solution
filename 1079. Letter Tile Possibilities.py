class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """

        tiles = ''.join(sorted(tiles))
        used = [False] * len(tiles)

        result = set()

        def backtrack(start, current):
            if current:
                result.add(''.join(current))

            
            for i in range(len(tiles)):
                if used[i]:
                    continue
                
                if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                current.append(tiles[i])
                backtrack(0, current)
                used[i] = False
        
        backtrack(0, [])
        return len(result)
