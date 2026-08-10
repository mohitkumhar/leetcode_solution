class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        target = n // 3

        counter = {}
        res = []

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for key, value in counter.items():
            if value > target:
                res.append(key)

        return res
