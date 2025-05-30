class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        result = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                result.append(i)

        return result
