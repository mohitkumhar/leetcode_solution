func reverse(str string) string {
	s := []byte(str)
	i := 0
	j := len(str) - 1

	for i < j {
		s[i], s[j] = s[j], s[i]
		i++
		j--
	}
	return string(s)
}

func minInsertions(s string) int {
	n := len(s)
	str1 := s
	str2 := reverse(s)

	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, n+1)
		for j := 0; j <= n; j++ {
			dp[i][j] = 0
		}
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			if str1[i-1] == str2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}

	return len(s) - dp[n][n]
}