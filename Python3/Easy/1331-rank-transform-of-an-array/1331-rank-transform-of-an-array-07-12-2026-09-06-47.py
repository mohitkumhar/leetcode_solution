class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        count = {}
        rank = 1

        for num in sorted_arr:
            count[num] = rank
            rank += 1
        result = [count[i] for i in arr]

        return result
