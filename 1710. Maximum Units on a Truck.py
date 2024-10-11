class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key = lambda x: x[1], reverse=True)

        total_unit = 0
        
        for box, unit in boxTypes:
            
            box_to_take = min(box, truckSize)

            total_unit += box_to_take * unit
            truckSize -= box_to_take
        
        return total_unit
