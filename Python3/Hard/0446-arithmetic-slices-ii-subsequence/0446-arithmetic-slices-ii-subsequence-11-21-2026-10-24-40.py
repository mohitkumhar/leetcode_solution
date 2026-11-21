class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0
        counter = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                count_at_j = counter[j].get(diff, 0)

                counter[i][diff] = counter[i].get(diff, 0) + count_at_j + 1

                result += count_at_j

        return result
