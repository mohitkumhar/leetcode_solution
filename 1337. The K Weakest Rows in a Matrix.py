class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = {}
        for i in range(len(mat)):
            result[i] = mat[i].count(1)

        result = dict(sorted(result.items(), key=lambda item: item[1]))
        ans = []
        for key, value in result.items():
            if len(ans) == k:
                return ans
            ans.append(key)
        return ans