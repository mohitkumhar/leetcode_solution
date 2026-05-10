class Solution:

    def mergeSort(self, arr, l, r):

        def merge(left, mid, right):
            i = 0 
            j = 0
            k = left

            left_arr = arr[left: mid+1]
            right_arr = arr[mid+1: right+1]

            len1 = len(left_arr)
            len2 = len(right_arr)
            ans = []

            while i < len1 and j < len2:
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len1:
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len2:
                arr[k] = right_arr[j]
                j += 1
                k += 1

            return ans

        def solve(left, right):
            if left == right:
                return [arr[left]]
            
            mid = left + (right - left) // 2
            left_sorted = solve(left, mid)
            right_sorted = solve(mid + 1, right)
            
            sorted_arr = merge(left, mid, right)

            return sorted_arr

        return solve(l, r)
