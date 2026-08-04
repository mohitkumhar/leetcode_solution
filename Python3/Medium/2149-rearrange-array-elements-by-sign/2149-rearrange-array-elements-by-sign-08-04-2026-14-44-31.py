class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        posValues = []
        negValues = []

        for num in nums:
            if num < 0:
                negValues.append(num)
            else:
                posValues.append(num)

        k = 0
        i = 0
        while k < len(nums):

            nums[k] = posValues[i]
            k += 1

            nums[k] = negValues[i]
            k += 1

            i += 1

        return nums
