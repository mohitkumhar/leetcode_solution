class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        n = len(arr)
        seen_idx = set()

        while queue:
            idx = queue.pop()
            seen_idx.add(idx)

            if idx >= n or idx < 0:
                continue

            if arr[idx] == 0:
                return True
            else:
                if idx + arr[idx] not in seen_idx:
                    queue.append(idx + arr[idx])
                if idx - arr[idx] not in seen_idx:
                    queue.append(idx - arr[idx])

        return False
