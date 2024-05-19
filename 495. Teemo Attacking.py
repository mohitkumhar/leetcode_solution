class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        count = 0

        for i in range(1, len(timeSeries)):
            if (timeSeries[i] - timeSeries[i - 1]) >= duration:
                count += duration

            else:
                count += (timeSeries[i] - timeSeries[i - 1])

        count += duration

        return count
