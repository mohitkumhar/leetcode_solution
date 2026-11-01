class Solution:
    def floodFill( self, image: list[list[int]], sr: int, sc: int, color: int ) -> list[list[int]]:
        originalColor = image[sr][sc]

        if originalColor == color:
            return image

        queue = [(sr, sc)]
        directions = [[1,0],[0,1],[0,-1],[-1,0]]

        image[sr][sc] = color

        m = len(image)
        n = len(image[0])

        while queue:
            x, y = queue.pop(0)

            for direction in directions:
                newX = x + direction[0]
                newY = y + direction[1]

                if ( 0 <= newX < m and 0 <= newY < n and image[newX][newY] == originalColor ):
                    image[newX][newY] = color
                    queue.append((newX, newY))

        return image
