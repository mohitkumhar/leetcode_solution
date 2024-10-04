class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        result = {}

        result[keysPressed[0]] = releaseTimes[0]

        for i in range(1,len(releaseTimes)):
            result[keysPressed[i]] = max(result.get(keysPressed[i], 0), releaseTimes[i] - releaseTimes[i - 1])
        
        max_value = max(result.values())
    

        max_keys = [key for key, value in result.items() if value == max_value]
        
        return max(max_keys)