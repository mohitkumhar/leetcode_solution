class Solution:
    def numTeams(self, rating: List[int]) -> int:

        n = len(rating)
        count = 0

        for i in range(n):
            left_low = left_high = 0
            right_low = right_high = 0

            for j in range(i):
                if rating[j] < rating[i]:
                    left_low += 1
                elif rating[j] > rating[i]:
                    left_high += 1

            for k in range(i + 1, n):
                if rating[k] > rating[i]:
                    right_high += 1
                elif rating[k] < rating[i]:
                    right_low += 1

            count += left_low * right_high + left_high * right_low

        return count
