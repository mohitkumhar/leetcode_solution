class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def isPossible(k):
            diff = [0] * (n + 1)

            for i in range(k):
                left, right, val = queries[i]
                diff[left] += val
                if right + 1 < n:
                    diff[right + 1] -= val

            currSum = 0
            for i in range(n):
                currSum += diff[i]

                if nums[i] - currSum > 0:
                    return False

            return True

        n = len(nums)

        left = 0
        right = len(queries)

        if not isPossible(right):
            return -1

        while left < right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                right = mid
            else:
                left = mid + 1

        return left
