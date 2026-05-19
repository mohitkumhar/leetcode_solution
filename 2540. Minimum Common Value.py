class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2 = set(nums2)
        ans = []
        for num in nums1:
            if num in nums2:
                return num
                break
        return -1
