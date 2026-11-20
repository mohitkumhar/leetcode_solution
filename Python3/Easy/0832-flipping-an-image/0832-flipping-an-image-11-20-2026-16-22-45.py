class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        m = len(image)
        n = len(image[0])

        for i in range(m):
            for j in range(n):
                image[i][j] = 1 if image[i][j] == 0 else 0

                if j >= (n // 2):
                    image[i][j], image[i][n - 1 - j] = image[i][n - 1 - j], image[i][j]

        return image
