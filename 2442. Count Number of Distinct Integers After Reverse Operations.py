class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            seen.add(num)
            rev_num = int(str(num)[::-1])
            seen.add(rev_num)

        return len(seen)
