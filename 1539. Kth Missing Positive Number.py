class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        i = 1
        while len(missing) < k:
            if i not in arr:
                missing.append(i)
            
            i += 1
        
        return missing[k - 1]
