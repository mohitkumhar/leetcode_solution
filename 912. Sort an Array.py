class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1

            elif left[i] > right[j]:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])

        return result
