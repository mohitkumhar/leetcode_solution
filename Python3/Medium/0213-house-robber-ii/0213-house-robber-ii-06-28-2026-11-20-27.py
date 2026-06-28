class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_house(i, arr, memo):
            n = len(arr)
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]

            steal = arr[i] + rob_house(i + 2, arr, memo)
            skip = rob_house(i + 1, arr, memo)

            memo[i] = max(steal, skip)

            return memo[i]

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo1 = [-1 for _ in range(n)]
        memo2 = [-1 for _ in range(n)]

        return max(rob_house(0, nums[1:], memo1), rob_house(0, nums[:-1], memo2))
