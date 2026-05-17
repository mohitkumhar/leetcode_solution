#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		result = []
		n = len(s)
		
		def solve(i, sequence):
		    if i >= n:
		        result.append(sequence)
		        return None

		        result.append(sequence)

		  #  take
		    solve(i + 1, sequence + s[i])

		  #  skip
		    solve(i + 1, sequence)


		solve(0, "")
		result.sort()

		return result
