class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0

        for account in accounts:
            maximum = max(maximum, sum(account))
        
        return maximum
