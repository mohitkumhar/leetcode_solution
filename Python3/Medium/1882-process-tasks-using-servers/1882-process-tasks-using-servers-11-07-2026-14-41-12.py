class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        freeServers = []  # serverWeight, idx

        for idx, server in enumerate(servers):
            heapq.heappush(freeServers, (server, idx))

        workingServers = []  # endTime, serverWeight, idx

        answer = [0] * len(tasks)

        for i in range(len(tasks)):

            # remove working server which is now idle
            while workingServers and workingServers[0][0] <= i:
                taskEndTime, serverWeight, idx = heapq.heappop(workingServers)
                heapq.heappush(freeServers, (serverWeight, idx))

            # hanldle if no free server is available
            if not freeServers:
                endTime, serverWeight, idx = heapq.heappop(workingServers)
                finalTime = endTime + tasks[i]

                heapq.heappush(workingServers, (finalTime, serverWeight, idx))
                answer[i] = idx

            # use the free server
            elif freeServers:
                serverWeight, idx = heapq.heappop(freeServers)

                taskEndTime = i + tasks[i]
                heapq.heappush(workingServers, (taskEndTime, serverWeight, idx))

                answer[i] = idx

        return answer
