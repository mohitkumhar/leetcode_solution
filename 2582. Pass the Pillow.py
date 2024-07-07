class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pillow_position = 1
        current_time = 0
        reverse_direction = False

        while current_time < time:
            if reverse_direction:
                pillow_position -= 1
            else:
                pillow_position += 1
            
            if pillow_position == 1:
                reverse_direction = False
            elif pillow_position == n:
                reverse_direction = True
            current_time += 1
            
            
        return pillow_position
        