class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = 0
        leftover = 0
        for key, value in count.items():
            result = result + value // 2
            leftover += value % 2

        return [result, leftover]