class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum % 2 == 1:
            return []

        ans = []
        currentSum = 2

        while finalSum >= currentSum:
            ans.append(currentSum)
            finalSum -= currentSum
            currentSum += 2
        
        if finalSum > 0:
            ans[-1] += finalSum

        return ans
        