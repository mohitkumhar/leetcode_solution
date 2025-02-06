class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        counter = {}

        for char in s:
            if char in counter:
                counter[char] += 1
            
            else:
                counter[char] = 1
        
        temp = list(counter.values())[0]

        for val in counter.values():
            if val != temp:
                return False
        return True



        