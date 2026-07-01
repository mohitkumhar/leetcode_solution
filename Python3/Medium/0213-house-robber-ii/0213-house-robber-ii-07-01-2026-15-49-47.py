class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo1 = [-1] * (n + 1)
        memo2 = [-1] * (n + 1)

        def rob_house(i, nums, memo):
            n = len(nums)
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]

            steal = nums[i] + rob_house(i + 2, nums, memo)
            skip = rob_house(i + 1, nums, memo)

            memo[i] = max(steal, skip)
            return memo[i]

        a = rob_house(0, nums[1:], memo1)
        b = rob_house(0, nums[:-1], memo2)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(a, b)

