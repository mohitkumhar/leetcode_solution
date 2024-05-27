class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total_jumps = 0
        final_destination = len(nums) - 1
        coverage = 0
        last_jump = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            coverage = max(coverage, i + nums[i])

            if i == last_jump:
                if coverage >= final_destination:
                    total_jumps += 1
                    return total_jumps

                last_jump = coverage
                total_jumps += 1
