class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(current_permutation, remaining_nums, result):
            if not remaining_nums:
                result.append(current_permutation[:])
                return


            for i in range(len(remaining_nums)):
                num = remaining_nums[i]

                current_permutation.append(num)
                backtrack(current_permutation, remaining_nums[i+1:] + remaining_nums[:i], result)
                current_permutation.pop()


        result = []

        backtrack([], nums, result)

        return result
