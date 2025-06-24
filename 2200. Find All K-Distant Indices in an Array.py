class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
        js = []

        for j in range(len(nums)):
            if nums[j] == key:
                js.append(j)

        for j in js:
            for i in range(len(nums)):
                if abs(i - j) <= k:
                    result.add(i)

        return sorted(result)
