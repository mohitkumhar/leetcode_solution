class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i, prev, curr_subseq):
            seen = set()
            if len(curr_subseq) >= 2:
                result.append(curr_subseq[:])

            for k in range(i, n):
                if prev == -1 or nums[k] >= nums[prev]:
                    if nums[k] in seen:
                        continue

                    curr_subseq.append(nums[k])
                    seen.add(nums[k])

                    backtrack(k + 1, k, curr_subseq)
                    curr_subseq.pop()

        result = []
        n = len(nums)

        backtrack(0, -1, [])

        return result
