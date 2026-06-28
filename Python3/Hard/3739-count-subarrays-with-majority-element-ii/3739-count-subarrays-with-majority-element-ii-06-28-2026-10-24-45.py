class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cum_sum = 0
        map = {0:1}
        valid_left_subarray = 0
        result = 0

        for j in range(n):
            if nums[j] == target:
                valid_left_subarray += map.get(cum_sum, 0)
                cum_sum += 1
            else:
                cum_sum -= 1
                valid_left_subarray -= map.get(cum_sum, 0)

            map[cum_sum] = map.get(cum_sum, 0) + 1
            result += valid_left_subarray

        return result

            




