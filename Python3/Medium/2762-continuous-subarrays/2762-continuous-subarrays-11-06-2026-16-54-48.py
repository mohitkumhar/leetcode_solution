class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        i = 0
        j = 0

        maxVal = []
        minVal = []

        while j < n:

            while maxVal and nums[j] > maxVal[-1]:
                maxVal.pop()
            maxVal.append(nums[j])

            while minVal and nums[j] < minVal[-1]:
                minVal.pop()
            minVal.append(nums[j])

            while maxVal[0] - minVal[0] > 2:
                if maxVal[0] == nums[i]:
                    maxVal.pop(0)
                if minVal[0] == nums[i]:
                    minVal.pop(0)
                i += 1

            if (maxVal[0] - minVal[0]) <= 2:
                result += (j - i + 1)

            j += 1

        return result
