class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sort_arr = sorted(set(arr))

        mapping = {}

        rank = 1

        for i in sort_arr:
            mapping[i] = rank
            rank += 1

        ans = [mapping[i] for i in arr]

        return ans