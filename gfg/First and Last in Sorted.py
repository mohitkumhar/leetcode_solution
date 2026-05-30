class Solution:
    def find(self, arr, x):
        n = len(arr)
        left = 0 
        right = n - 1
        start = -1
        end = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == x:
                start = mid
                end = mid

                while mid > 0 and arr[mid - 1] == x:
                    mid -= 1
                    start = mid

                while (mid + 1) < n and arr[mid + 1] == x:
                    mid += 1
                    end = mid
                break

            elif arr[mid] < x:
                left = mid + 1

            else:
                right = mid - 1
        
        return [start, end]
