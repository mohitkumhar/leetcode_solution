class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {ch: i for i, ch in enumerate(s)}

        end = 0
        start = 0
        result = []
        for i, ch in enumerate(s):
            end = max(end, map[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
