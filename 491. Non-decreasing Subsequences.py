class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            if len(path) >= 2:
                res.append(path[:])

            used = set()
            for i in range(start, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in used:
                    continue
                used.add(nums[i])
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res