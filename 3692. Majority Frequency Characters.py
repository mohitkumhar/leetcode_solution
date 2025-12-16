class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        counter = {}
        for c, f in freq.items():
            if f in counter.keys():
                counter[f].append(c)
            else:
                counter[f] = [c]

        ans = ('', 0)
        print(counter)
        for key, value in counter.items():
            if len(value) > len(ans[0]):
                ans = (''.join(value), key)
            elif len(value) == len(ans[0]):
                ans = ans if ans[1] > key else (''.join(value), key)

        return ans[0]
