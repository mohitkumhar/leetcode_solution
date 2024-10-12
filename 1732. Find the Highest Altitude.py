class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        max_altitude = 0

        temp = 0
        
        for i in range(len(gain)):
            temp += gain[i]

            max_altitude = max(max_altitude, temp)
        
        return max_altitude
