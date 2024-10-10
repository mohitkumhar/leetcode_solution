class Solution:
    def numberOfMatches(self, n: int) -> int:
        team = n
        total_matches = 0

        while team != 1:
            matches = team // 2
            
            total_matches += matches

            if team % 2 == 0:
                team = team // 2
            else:
                team = team // 2 + 1
            
        return total_matches
