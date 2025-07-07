class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)

        subset = []
        subset_sum = 0
        for num in nums:
            subset.append(num)
            subset_sum += num

            if subset_sum > total - subset_sum:
                break
        return subset