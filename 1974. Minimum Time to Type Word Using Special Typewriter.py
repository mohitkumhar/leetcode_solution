class Solution:
    def minTimeToType(self, word: str) -> int:

        current_pos = 0
        time = 0

        for char in word:
            target_pos = ord(char) - ord('a')

            distance = abs(current_pos - target_pos)

            time += min(distance, 26 - distance)

            time += 1

            current_pos = target_pos
        
        return time
