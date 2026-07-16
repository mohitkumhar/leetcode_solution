class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_seen = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > max_seen:
                max_seen = nums[i]
            nums[i] = math.gcd(nums[i], max_seen)

        i = 0
        j = n - 1
        result = 0
        nums.sort()

        while i < j:
            result += math.gcd(nums[i], nums[j])
            i += 1
            j -= 1

        return result
