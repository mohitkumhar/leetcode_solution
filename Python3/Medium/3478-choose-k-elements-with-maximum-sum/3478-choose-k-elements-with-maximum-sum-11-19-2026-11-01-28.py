class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        n = len(nums1)
        heap = []

        for i in range(n):
            heapq.heappush(heap, (nums1[i], i))

        answer = [0] * n

        currSum = 0
        currSumHeap = []

        prevNum = -1
        prevSum = 0

        while heap:
            num, idx = heapq.heappop(heap)

            if num == prevNum:
                answer[idx] = prevSum
            else:
                answer[idx] = currSum
                prevNum = num
                prevSum = currSum

            heapq.heappush(currSumHeap, nums2[idx])
            currSum += nums2[idx]
            if len(currSumHeap) > k:
                currSum -= heapq.heappop(currSumHeap)

        return answer
