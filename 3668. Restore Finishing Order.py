class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        ans = []
        for item in order:
            if item in friends:
                ans.append(item)
        return ans
