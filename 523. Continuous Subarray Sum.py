class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = {0: -1}
        cum_sum = 0
        for i, num in enumerate(nums):

            cum_sum += num
            mod = cum_sum % k

            if mod in count:
                if i - count[mod] > 1:
                    return True
            else:
                count[mod] = i

        return False
