class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        zero_edge = edges[0]
        first_edge = edges[1]

        a = list(set(zero_edge).intersection(first_edge))

        return a[0]
