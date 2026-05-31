class Solution:
    def countFreq(self, arr, target):
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                count = 1
                
                temp = mid
                while temp > 0 and arr[temp - 1] == target:
                    count += 1
                    temp -= 1
                
                temp = mid
                while temp < (n - 1) and arr[temp + 1] == target:
                    count += 1
                    temp += 1
                
                return count

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return 0
