class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n // 3

        result = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            if value > target:
                result.append(key)

        return result
