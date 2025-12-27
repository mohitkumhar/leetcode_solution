class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        def isValid(x, y, numRow, numCol):
            return x >= 0 and x < numRow and y >= 0 and y < numCol

        queue = [(sr, sc)]
        numRow = len(image)
        numCol = len(image[0])
        curr_color = image[sr][sc]

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while queue:
            current_color_i, current_color_j = queue.pop()
            image[current_color_i][current_color_j] = color

            for direction in directions:
                new_color_i = current_color_i + direction[0]
                new_color_j = current_color_j + direction[1]

                if isValid(new_color_i, new_color_j, numRow, numCol) and image[new_color_i][new_color_j] == curr_color:
                    queue.append((new_color_i, new_color_j))
                    image[new_color_i][new_color_j] = color
        
        return image
