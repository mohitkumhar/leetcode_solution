class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}
        min_len = len(arr) // 2
        total_len = len(arr)

        for i in range(len(arr)):
            if arr[i] in counter:
                counter[arr[i]] += 1
            else:
                counter[arr[i]] = 1

        counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        count = 0

        for key, items in counter.items():
            if total_len > min_len:
                count += 1
                total_len -= items
        return count
