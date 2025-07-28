class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        arr = []
        for num in nums:
            if num in seen:
                arr.append(num)
            else:
                seen.add(num)
        if not arr:
            return 0

        result = 0
        for num in arr:
            result ^= num
        return result
