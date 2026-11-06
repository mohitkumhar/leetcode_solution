class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:

        logs.sort(key=lambda x: x[1])

        query = [(queries[i], i) for i in range(len(queries))]
        query.sort(key=lambda x: x[0])

        i = 0
        j = 0
        answer = [0] * len(query)
        freq = {}

        for time, ind in query:
            startTime = time - x
            endTime = time

            while j < len(logs) and logs[j][1] <= endTime:
                freq[logs[j][0]] = freq.get(logs[j][0], 0) + 1
                j += 1

            while i < len(logs) and logs[i][1] < startTime:
                freq[logs[i][0]] -= 1
                if freq[logs[i][0]] == 0:
                    del freq[logs[i][0]]
                i += 1

            answer[ind] = n - len(freq)

        return answer
