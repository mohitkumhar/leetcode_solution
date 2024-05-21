class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        n = len(cost)

        if n == 0 or n == 1:
            return 0

        prev1 = cost[1]
        prev2 = cost[0]

        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current

        return min(prev1, prev2)
