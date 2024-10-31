class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seen = set()
        reviewed = set()

        for start in range(len(s) - 9):
            window = s[start: start + 10]

            if window in seen:
                reviewed.add(window)
            
            else:
                seen.add(window)
        
        return list(reviewed)
