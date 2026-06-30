class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = []
        positive = []
        negative = []

        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)

        pos_idx = 0
        neg_idx = 0
        for i in range(n):
            if i % 2 == 0:
                answer.append(positive[pos_idx])
                pos_idx += 1
            else:
                answer.append(negative[neg_idx])
                neg_idx += 1

        return answer
