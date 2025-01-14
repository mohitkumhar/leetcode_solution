class Solution:
    def minSwaps(self, s: str) -> int:
        
        balance = 0
        max_balance = 0

        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                max_balance = max(max_balance, -balance)
                
        swaps = (max_balance + 1) // 2   # " +1 " for handling the odd values, and it does not affact the even values, "/ 2" because each swap corrects the 2 brackets

        return swaps
