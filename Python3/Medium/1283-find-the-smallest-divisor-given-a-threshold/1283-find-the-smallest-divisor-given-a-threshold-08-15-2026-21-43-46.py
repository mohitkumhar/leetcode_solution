class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isPossible(val, nums, threshold):
            count = 0

            for num in nums:
                flag = 0

                if num % val != 0:
                    flag = 1

                count += (num // val) + flag

            return count <= threshold

        n = len(nums)

        left = 1
        right = max(nums)

        while left < right:
            mid = left + (right - left) // 2

            if isPossible(mid, nums, threshold):
                right = mid
            else:
                left = mid + 1

        return left
