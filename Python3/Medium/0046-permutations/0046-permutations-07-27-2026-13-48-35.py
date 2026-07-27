class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, curr_perm):
            if len(curr_perm) == len(nums):
                result.append(curr_perm[:])
                return

            for j in range(len(nums)):
                if nums[j] in seen:
                    continue

                curr_perm.append(nums[j])
                seen.add(nums[j])

                backtrack(j + 1, curr_perm)

                curr_perm.pop()
                seen.remove(nums[j])

        result = []
        seen = set()
        backtrack(0, [])

        return result
