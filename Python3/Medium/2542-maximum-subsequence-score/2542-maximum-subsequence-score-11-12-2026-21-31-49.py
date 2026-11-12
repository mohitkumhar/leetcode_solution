class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n = len(nums1)

        nums = []

        for i in range(n):
            nums.append((nums1[i], nums2[i]))

        nums.sort(key=lambda x: x[1], reverse=True)

        minKElements = []
        currKElementsSum = 0

        for i in range(k):
            heapq.heappush(minKElements, nums[i][0])
            currKElementsSum += nums[i][0]

        ans = nums[k - 1][1] * currKElementsSum

        for i in range(k, n):
            nums2Min = nums[i][1]

            if nums[i][0] > minKElements[0]:
                currMinElement = heapq.heappop(minKElements)
                currKElementsSum -= currMinElement

                heapq.heappush(minKElements, nums[i][0])
                currKElementsSum += nums[i][0]

            ans = max(ans, nums2Min * currKElementsSum)

        return ans
