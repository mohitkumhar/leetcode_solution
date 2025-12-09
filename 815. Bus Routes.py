class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type: routes: List[List[int]]
        :type: source: int
        :type: target: int
        :rtype: int
        """
        counter = {}

        for i in range(len(routes)):
            for stop in routes[i]:
                if stop not in counter:
                    counter[stop] = []
                counter[stop].append(i)

        queue = [source]
        busVisited = set()
        stopVisited = set()
        min_bus = 0

        while queue:
            size = len(queue)
            for i in range(size):
                curr_stop = queue.pop(0)

                if curr_stop == target:
                    return min_bus

                for bus in counter.get(curr_stop, []):

                    if bus not in busVisited:
                        for stop in routes[bus]:
                            if stop not in stopVisited:
                                queue.append(stop)
                                stopVisited.add(stop)
                        busVisited.add(bus)
            min_bus += 1

        return -1
