class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        answer = []
        nums.sort()

        for query in queries:
            count = 0
            currSum = 0

            for num in nums:
                currSum += num
                if currSum <= query:
                    count += 1
                else:
                    break

            answer.append(count)

        return answer
