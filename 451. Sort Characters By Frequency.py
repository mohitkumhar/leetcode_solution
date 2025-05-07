class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        count = dict(sorted(count.items(), key = lambda x: -x[1]))
        ans = ''

        for key, value in count.items():
            ans += (key * value)

        return ans