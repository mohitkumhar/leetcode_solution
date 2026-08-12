class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def countPairs(left, mid, right, nums):
            count = 0
            j = mid + 1

            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count = count + (j - (mid + 1))
            return count

        def merge(left, mid, right, nums):
            nums1 = nums[left : mid + 1]
            nums2 = nums[mid + 1 : right + 1]

            len1 = len(nums1)
            len2 = len(nums2)

            i = 0
            j = 0

            k = left

            while i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    nums[k] = nums1[i]
                    i += 1
                else:
                    nums[k] = nums2[j]
                    j += 1
                k += 1

            while i < len1:
                nums[k] = nums1[i]
                i += 1
                k += 1

            while j < len2:
                nums[k] = nums2[j]
                j += 1
                k += 1

        def mergeSort(left, right, nums):
            if left >= right:
                return 0

            count = 0

            mid = left + (right - left) // 2

            count += mergeSort(left, mid, nums)
            count += mergeSort(mid + 1, right, nums)

            count += countPairs(left, mid, right, nums)

            merge(left, mid, right, nums)

            return count

        n = len(nums)
        count = mergeSort(0, n - 1, nums)

        return count
