class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def findMinSumIndex():
            index = 0
            minSum = nums[0] + nums[1]

            for i in range(1, len(nums) - 1):
                currSum = nums[i] + nums[i + 1]

                if currSum < minSum:
                    minSum = currSum
                    index = i

            return index

        operation = 0

        while True:

            isSorted = True

            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    isSorted = False
                    break

            if isSorted:
                return operation

            index = findMinSumIndex()

            nums[index] = nums[index] + nums[index + 1]
            nums.pop(index + 1)

            operation += 1
