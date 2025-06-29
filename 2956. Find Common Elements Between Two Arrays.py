class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans1 = 0
        ans2 = 0
        for num in nums1:
            if num in nums2:
                ans1 += 1

        for num in nums2:
            if num in nums1:
                ans2 += 1

        return [ans1, ans2]