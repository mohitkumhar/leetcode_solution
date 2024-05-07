class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """

        candy_can_be_eaten = len(candyType) // 2
        non_common_candy = len(set(candyType))

        return min(non_common_candy, candy_can_be_eaten)