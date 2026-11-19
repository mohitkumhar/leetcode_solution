class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        n = N // 3

        leftMinSum = [0] * N
        rightMaxSum = [0] * N

        maxHeap = []
        leftSum = 0

        for i in range(2 * n):
            heapq.heappush(maxHeap, -nums[i])
            leftSum += nums[i]

            if len(maxHeap) > n:
                leftSum -= -heapq.heappop(maxHeap)

            leftMinSum[i] = leftSum

        minHeap = []
        rightSum = 0

        for i in range(N - 1, n - 1, -1):
            heapq.heappush(minHeap, nums[i])
            rightSum += nums[i]

            if len(minHeap) > n:
                rightSum -= heapq.heappop(minHeap)

            rightMaxSum[i] = rightSum

        result = float('inf')

        for i in range(n - 1, 2 * n):
            result = min(result, leftMinSum[i] - rightMaxSum[i + 1])

        return result