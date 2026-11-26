class Solution:
    def canAliceWin(self, n: int) -> bool:
        chance = 10
        turn = False

        while n > 0:
            n -= chance

            if n < 0:
                return turn

            turn = True if turn == False else False
            chance -= 1

        return turn
