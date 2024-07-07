class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles

        while numBottles >= numExchange:
            extra_bottles = numBottles % numExchange
            new_water_bottles = numBottles // numExchange

            drink += new_water_bottles

            numBottles = extra_bottles + new_water_bottles

        return drink
