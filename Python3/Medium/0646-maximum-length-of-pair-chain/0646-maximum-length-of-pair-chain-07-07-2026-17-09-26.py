class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        prev_end = -1001
        count = 0

        for pair in pairs:
            curr_front = pair[0]

            if prev_end < curr_front:
                count += 1
                prev_end = pair[1]

        return count
