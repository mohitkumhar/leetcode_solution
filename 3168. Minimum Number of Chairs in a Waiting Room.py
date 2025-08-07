class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chairs = 0
        counter = 0

        for char in s:
            if char == 'E':
                counter += 1
            else:
                counter -= 1
            max_chairs = max(max_chairs, counter)
        return max_chairs