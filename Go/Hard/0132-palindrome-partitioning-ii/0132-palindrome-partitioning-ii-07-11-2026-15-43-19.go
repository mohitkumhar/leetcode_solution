func minCut(s string) int {
	n := len(s)
	dp := make([][]bool, n)

	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
	}

	for L := 1; L <= n; L++ {
		for i := 0; i+L-1 < n; i++ {
			j := i + L - 1

			if L == 1 {
				dp[i][j] = true
			} else if L == 2 {
				dp[i][j] = s[i] == s[j]
			} else {
				dp[i][j] = s[i] == s[j] && dp[i+1][j-1]
			}
		}
	}

	dp_cuts := make([]int, n)
	for i := 0; i < n; i++ {
		dp_cuts[i] = math.MaxInt
	}
	dp_cuts[0] = 0

	for i := 0; i < n; i++ {
		if dp[0][i] {
			dp_cuts[i] = 0
		}
		for k := 0; k < i; k++ {
			if dp[k+1][i] {
				curr_cut := 1 + dp_cuts[k]
				dp_cuts[i] = min(dp_cuts[i], curr_cut)
			}
		}
	}

	return dp_cuts[n-1]
}