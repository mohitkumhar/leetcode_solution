class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        missing = -1
        for i in range(1, n + 1):
            if i not in seen:
                missing = i

        return [duplicate, missing]
