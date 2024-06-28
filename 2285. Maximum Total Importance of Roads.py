class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        count = {i: 0 for i in range(n)}

        for road in roads:
            count[road[0]] += 1
            count[road[1]] += 1

        check = [i for i in count.values()]

        check.sort(reverse=True)

        ans = 0

        for i in range(n):
            ans += check[i] * (n - i)

        return ans
