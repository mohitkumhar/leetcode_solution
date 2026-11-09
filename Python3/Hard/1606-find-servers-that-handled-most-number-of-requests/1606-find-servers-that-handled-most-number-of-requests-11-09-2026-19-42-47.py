class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        availableServers = SortedSet()
        for i in range(k):
            availableServers.add(i)

        runningServers = []  # heap [ taskEndTime, serverId ]
        servers = [0] * k

        for i in range(len(arrival)):

            # removed free server from the running servers

            while runningServers and runningServers[0][0] <= arrival[i]:
                taskEndTime, serverIdx = heapq.heappop(runningServers)
                availableServers.add(serverIdx)

            if not availableServers:
                continue

            # fetch the recommended server
            recServer = i % k

            # get free server for the task
            freeServerId = availableServers.bisect_left(recServer)
            if freeServerId == len(availableServers):
                freeServerId = 0

            freeServer = availableServers[freeServerId]

            # add this free server to the running servers and remove it from available server
            availableServers.remove(freeServer)

            currTaskEndTime = arrival[i] + load[i]

            heapq.heappush(runningServers, (currTaskEndTime, freeServer))
            servers[freeServer] += 1

        busiestServer = max(servers)

        return [i for i in range(len(servers)) if servers[i] == busiestServer]
