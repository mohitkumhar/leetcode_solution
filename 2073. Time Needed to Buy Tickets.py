class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        time = 0
        
        i = 0
        while tickets[k] > 0:
            if tickets[i] != 0:
                tickets[i] -= 1
                time += 1
            i = (i + 1) % len(tickets)

        
        return time


        