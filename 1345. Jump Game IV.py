class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        counter = {}
        for i, num in enumerate(arr):
            if num not in counter:
                counter[num] = []
            counter[num].append(i)

        queue = [0]
        visited = set()
        steps = 0

        while queue:
            size = len(queue)

            while size!=0:
                ind = queue.pop(0)

                if ind == n - 1:
                    return steps

                if ind > 0 and ind - 1 not in visited:
                    visited.add(ind - 1)
                    queue.append(ind - 1)
                if ind < n - 1 and ind + 1 not in visited:
                    visited.add(ind + 1)
                    queue.append(ind + 1)

                if arr[ind] in counter:
                    for key in counter[arr[ind]]:
                        print("key ", key)
                        if key not in visited:
                            visited.add(key)
                            queue.append(key)
                    del counter[arr[key]]

                size -= 1
            steps += 1

        return steps
