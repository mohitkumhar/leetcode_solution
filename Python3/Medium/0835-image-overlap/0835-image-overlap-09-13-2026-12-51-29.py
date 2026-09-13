class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        def countOverlap(rowRange, colRange):
            count = 0

            for row in range(0, n):
                for col in range(0, n):
                    if (
                        row + rowRange < 0
                        or row + rowRange >= n
                        or col + colRange < 0
                        or col + colRange >= n
                    ):
                        continue

                    if img1[row][col] == 1 and img2[row + rowRange][col + colRange]:
                        count += 1

            return count

        n = len(img1)
        maxOverlap = 0

        for rowRange in range(-n + 1, n):
            for colRange in range(-n + 1, n):
                maxOverlap = max(maxOverlap, countOverlap(rowRange, colRange))

        return maxOverlap
