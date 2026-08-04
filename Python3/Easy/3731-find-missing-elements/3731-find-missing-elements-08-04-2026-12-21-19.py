class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxElement = max(nums)
        minElement = min(nums)

        nums = set(nums)
        answer = []

        for i in range(minElement, maxElement + 1):
            if i not in nums:
                answer.append(i)

        return answer
