class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isPossible(maxVal):
            currVal = 0
            subArrayCount = 1

            for num in nums:
                if (num + currVal) > maxVal:
                    subArrayCount += 1
                    currVal = num
                else:
                    currVal += num

            return subArrayCount <= k

        left = max(nums)
        right = sum(nums)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans
