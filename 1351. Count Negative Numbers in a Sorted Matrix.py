class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in grid:
            print(i)
            for j in i:
                if j < 0:
                    ans += 1
 
        return ans
