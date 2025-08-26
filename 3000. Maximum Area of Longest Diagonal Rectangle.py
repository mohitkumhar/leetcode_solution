class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        result = []
        max_val = 0
        for dim in dimensions:
            temp = sqrt(dim[0] * dim[0] + dim[1] * dim[1])
            if temp > max_val:
                max_val = temp
                ans = dim[0] * dim[1]
            if temp == max_val:
                ans = max(ans, dim[0] * dim[1])
        return ans