class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1


        count = dict(sorted(freq.items(), key=lambda x: -x[1]))
        ans = ""

        for key, value in count.items():
            ans += key * value

        return ans
