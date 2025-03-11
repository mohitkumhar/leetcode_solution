class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        start = 0
        end = k - 1
        blocks = list(blocks)
        min_black = 100


        for i in range(len(blocks)):
            min_black = min(min_black, blocks[start: end + 1].count('W'))

            start += 1
            end += 1

            if end == len(blocks):
                break
        return min_black
