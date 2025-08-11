class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counter = {}
        nums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        result = []
        for key, value in counter.items():
            if value >= 2:
                result.append(key)
        return list(set(result))