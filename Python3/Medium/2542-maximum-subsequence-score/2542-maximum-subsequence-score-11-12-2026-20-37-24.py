class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n = len(nums1)
        nums = []

        for i in range(n):
            nums.append((nums1[i], nums2[i]))

        minKElements = []
        minKElementsSum = 0

        nums.sort(key=lambda x: x[1], reverse=True)

        for i in range(k):
            heapq.heappush(minKElements, nums[i][0])
            minKElementsSum += nums[i][0]

        ans = nums[k - 1][1] * minKElementsSum

        for i in range(k, n):
            currNums2Min = nums[i][1]

            if minKElements[0] < nums[i][0]:
                minElementInHeap = heapq.heappop(minKElements)
                minKElementsSum -= minElementInHeap

                heapq.heappush(minKElements, nums[i][0])
                minKElementsSum += nums[i][0]

            ans = max(ans, currNums2Min * minKElementsSum)

        return ans
