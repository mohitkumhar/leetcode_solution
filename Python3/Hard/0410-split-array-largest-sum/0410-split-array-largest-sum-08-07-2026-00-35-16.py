class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def isSplit(maxVal):
            count = 1
            currSum = 0

            for num in nums:
                if currSum + num > maxVal:
                    count += 1
                    currSum = num

                else:
                    currSum += num

            return count <= k

        n = len(nums)

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2

            if isSplit(mid):
                right = mid
            else:
                left = mid + 1

        return right
