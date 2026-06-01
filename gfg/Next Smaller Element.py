class Solution:
	def nextSmallerEle(self, arr):
		stack = []
		ans = []
		n = len(arr)

		for i in range(n - 1, -1, -1):
		    while stack and stack[-1] >= arr[i]:
		        stack.pop()

		    if not stack:
		        ans.append(-1)

            elif stack[-1] < arr[i]:
                ans.append(stack[-1])

            stack.append(arr[i])

        return ans[::-1]
