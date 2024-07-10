class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for log in logs:
            if log == './':
                pass  # Remain in same folder
            
            elif log == '../':
                if count > 0:
                    count -= 1
            
            else:
                count += 1
        return count

        