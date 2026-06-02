class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """

        def calculate(start1, end1, start2, end2):
            earlist_end_time = min(start1[i] + end1[i] for i in range(len(start1)))

            min_time = float("inf")
            for i in range(len(start2)):
                late_end_time = max(earlist_end_time, start2[i]) + end2[i]
                min_time = min(min_time, late_end_time)

            return min_time


        # land -> water
        land_to_water = calculate(landStartTime, landDuration, waterStartTime, waterDuration)

        # water -> land
        water_to_land = calculate(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_to_water, water_to_land)
