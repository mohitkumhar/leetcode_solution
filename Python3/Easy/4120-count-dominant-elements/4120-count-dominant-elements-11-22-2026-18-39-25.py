class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        गिनती = 0

        for i in range(n):

            if i == 0 and i == n - 1:
                गिनती += 1

            elif i == 0:
                if nums[i] >= nums[i + 1]:
                    गिनती += 1

            elif i == n - 1:
                if nums[i] >= nums[i - 1]:
                    गिनती += 1

            else:
                avg = (nums[i - 1] + nums[i + 1]) / 2
                if nums[i] >= avg:
                    गिनती += 1

        return गिनती
