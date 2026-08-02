class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        k = 0
        seen = set()

        for i in range(n):

            if nums[i] in seen:
                continue

            nums[k] = nums[i]
            k += 1

            seen.add(nums[i])
        return k