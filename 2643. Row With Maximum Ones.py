class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0, 0]
        for ind, i in enumerate(mat):
            if i.count(1) > res[0]:
                res[0] = i.count(1)
                res[1] = ind

        return res[::-1]