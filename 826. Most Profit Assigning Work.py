class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        max_profit = 0
        job_index = 0
        best_profit = 0

        for ability in worker:
            while job_index < len(jobs) and ability >= jobs[job_index][0]:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1

            max_profit += best_profit

        return max_profit
