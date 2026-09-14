class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        events = [0] * n

        for request in requests:
            events[request[0]] += 1
            if request[1] + 1 < n:
                events[request[1] + 1] -= 1

        for i in range(1, len(events)):
            events[i] += events[i - 1]

        events.sort(reverse=True)
        nums.sort(reverse=True)

        prod = 0
        for i in range(n):
            prod += (nums[i] * events[i]) % MOD

        return prod % MOD
