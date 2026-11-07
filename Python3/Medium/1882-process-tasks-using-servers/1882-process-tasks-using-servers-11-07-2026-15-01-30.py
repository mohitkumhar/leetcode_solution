class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        freeServers = []  # serverWeight, idx

        for i, server in enumerate(servers):
            heapq.heappush(freeServers, (server, i))

        busyServers = []  # freeTime, serverWeight, idx

        answer = [0] * len(tasks)

        for i in range(len(tasks)):

            while busyServers and busyServers[0][0] <= i:
                taskEndTime, serverWeight, idx = heapq.heappop(busyServers)
                heapq.heappush(freeServers, (serverWeight, idx))

            if freeServers:
                serverWeight, idx = heapq.heappop(freeServers)
                taskEndTime = i + tasks[i]

                heapq.heappush(busyServers, (taskEndTime, serverWeight, idx))

                answer[i] = idx

            elif not freeServers:
                taskEndTime, serverWeight, idx = heapq.heappop(busyServers)
                newTaskEndTime = taskEndTime + tasks[i]

                heapq.heappush(busyServers, (newTaskEndTime, serverWeight, idx))

                answer[i] = idx

        return answer
