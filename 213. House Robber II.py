class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solve(nums):
            n = len(nums)
            self.result = [0] * n
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])

            self.result[0] = nums[0]
            self.result[1] = max(nums[0], nums[1])

            for i in range(2, n):
                steal = nums[i] + self.result[i - 2]
                skip = self.result[i-1]

                self.result[i] = max(steal, skip)

            return self.result[n-1]

        use_0th_ind = solve(nums[:-1])
        use_1st_ind = solve(nums[1:])

        return max(use_1st_ind, use_0th_ind)
