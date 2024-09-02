class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        result = []
        for val in count.values():
            result.append(val)
        
        return len(result) == len(set(result))
