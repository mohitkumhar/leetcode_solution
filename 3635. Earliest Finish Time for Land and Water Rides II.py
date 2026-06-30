class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        def calculate(start_time_1, end_time_1, start_time_2, end_time_2):
            earliest_finish_ride_1 = float("inf")
            for i in range(len(start_time_1)):
                earliest_finish_ride_1 = min(earliest_finish_ride_1, start_time_1[i] + end_time_1[i])    

            earliest_finish_ride_2 = float("inf")

            for i in range(len(start_time_2)):
                ride_2_start_time = max(earliest_finish_ride_1, start_time_2[i]) + end_time_2[i]
                earliest_finish_ride_2 = min(earliest_finish_ride_2, ride_2_start_time)

            return earliest_finish_ride_2

        # land -> water
        land_to_water = calculate(landStartTime, landDuration, waterStartTime, waterDuration)

        # water - > land
        water_to_land = calculate(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_to_water, water_to_land)
