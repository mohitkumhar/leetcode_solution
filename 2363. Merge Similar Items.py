class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        counter = {}
        for value, weight in items1 + items2:
            if value in counter:
                counter[value] += weight
            else:
                counter[value] = weight

        result = []
        for key, values in counter.items():
            result.append([key, values])
        return sorted(result, key=lambda x: x[0])
