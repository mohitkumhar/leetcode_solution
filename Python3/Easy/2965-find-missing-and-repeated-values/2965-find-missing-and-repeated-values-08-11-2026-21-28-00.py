class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
            n = len(grid)
        
            # find duplicate
            duplicate = -1
            seen = set()
            
            for lst in grid:
                for num in lst:
                    if num in seen:
                        duplicate = num
                    else:
                        seen.add(num)

            # find missing number
            missingNumber = -1
            for i in range(1, n * n + 1):
                if i not in seen:
                    missingNumber = i
                    break

            return [duplicate, missingNumber]