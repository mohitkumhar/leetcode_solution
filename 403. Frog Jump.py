class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jump_pos = {stone: set() for stone in stones}
        jump_pos[0].add(1)
        destination = stones[-1]

        for stone in stones:
            for jump in jump_pos[stone]:
                next_position = stone + jump
                if next_position == destination: 
                    return True

                if next_position in stones:
                    if jump - 1 > 0:
                        jump_pos[next_position].add(jump - 1)
                    jump_pos[next_position].add(jump)
                    jump_pos[next_position].add(jump + 1)
        return False
