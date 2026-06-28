class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_house(arr):
            n = len(arr)
            next_prev = arr[0]
            prev = max(arr[0], arr[1])
            ans = prev

            for i in range(2, n):
                steal = arr[i] + next_prev
                skip = prev

                ans = max(steal, skip)
                next_prev = prev
                prev = ans

            return ans

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])


        return max(rob_house(nums[1:]), rob_house(nums[:-1]))

