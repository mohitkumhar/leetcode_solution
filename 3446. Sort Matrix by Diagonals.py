class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        counter = {}

        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in counter:
                    counter[key] = []
                counter[key].append(grid[i][j])
        
        for key, values in counter.items():
            if key < 0:
                values.sort()
            else:
                values.sort(reverse=True)
        
        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = counter[key].pop(0)
        return grid
