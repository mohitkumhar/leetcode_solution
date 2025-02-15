class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = 0
        result = []

        for char in seq:
            if char == '(':
                result.append(depth % 2)
                depth += 1

            else:
                depth -= 1
                result.append(depth % 2)
    
        return result
    