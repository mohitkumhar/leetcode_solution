class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        events = [0] * (n)

        for query in queries:
            start, end = query

            events[start] += 1
            if end + 1 < n:
                events[end + 1] -= 1

        for i in range(1, n):
            events[i] += events[i - 1]

        for i in range(n):
            if nums[i] > events[i]:
                return False
        return True
