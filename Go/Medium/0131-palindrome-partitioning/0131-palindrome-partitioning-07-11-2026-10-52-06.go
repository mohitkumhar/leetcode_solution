func solve(i int, s string, curr_str []string, result *[][]string, dp [][]bool) {
	if i == len(s) {
		temp := append([]string{}, curr_str...)
		*result = append(*result, temp)
		return
	}

	for j := i; j < len(s); j++ {
		if dp[i][j] == true {
			curr_str = append(curr_str, s[i:j+1])
			solve(j+1, s, curr_str, result, dp)
			if len(curr_str) > 0 {
				curr_str = curr_str[:len(curr_str)-1]
			}
		}
	}
}

func partition(s string) [][]string {
	n := len(s)

	dp := make([][]bool, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]bool, n+1)
	}

	for L := 1; L <= n; L++ {
		for i := 0; i+L-1 < n; i++ {
			j := i + L - 1

			if L == 1 {
				dp[i][j] = true
			} else if L == 2 {
				dp[i][j] = s[i] == s[j]
			} else {
				dp[i][j] = s[i] == s[j] && dp[i+1][j-1] == true
			}
		}
	}

	curr_str := []string{}
	result := [][]string{}
	i := 0

	solve(i, s, curr_str, &result, dp)

	return result
}