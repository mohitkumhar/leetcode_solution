func longestPalindrome(s string) string {
	n := len(s)
	max_pal := ""
	dp := make([][]bool, n)

	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
	}

	for L := 1; L <= n; L++ {
		for i := 0; (i + L - 1) < n; i++ {
			j := i + L - 1

			if L == 1 {
				dp[i][j] = true
			} else if L == 2 {
				dp[i][j] = s[i] == s[j]
			} else {
				dp[i][j] = s[i] == s[j] && dp[i+1][j-1]
			}
			if dp[i][j] == true {
				if L > len(max_pal) {
					max_pal = s[i : j+1]
				}
			}
		}
	}

	return max_pal
}