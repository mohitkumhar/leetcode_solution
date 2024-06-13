class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(start, checking_combination, combination_sum):
            if combination_sum == target:
                result.append(list(checking_combination))
                return

            if combination_sum > target:
                return

            for i in range(start, len(candidates)):
                checking_combination.append(candidates[i])

                backtrack(i, checking_combination,
                          combination_sum + candidates[i])

                checking_combination.pop()

        result = []

        backtrack(0, [], 0)

        return result
