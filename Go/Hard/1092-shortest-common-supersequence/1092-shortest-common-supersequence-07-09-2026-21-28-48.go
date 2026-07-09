func reverse(str []string) string {
	i := 0
	j := len(str) - 1

	for i < j {
		str[i], str[j] = str[j], str[i]
		i++
		j--
	}

	return strings.Join(str, "")
}

func shortestCommonSupersequence(str1 string, str2 string) string {
	m := len(str1)
	n := len(str2)

	dp := make([][]int, m+1)

	for i := 0; i <= m; i++ {
		dp[i] = make([]int, n+1)
		for j := 0; j <= n; j++ {
			dp[i][j] = 0
		}
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if str1[i-1] == str2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}

	i := m
	j := n
	result := make([]string, 0)

	for i > 0 && j > 0 {
		if str1[i-1] == str2[j-1] {
			result = append(result, string(str1[i-1]))
			i--
			j--
		} else {
			if dp[i-1][j] > dp[i][j-1] {
				result = append(result, string(str1[i-1]))
				i--
			} else {
				result = append(result, string(str2[j-1]))
				j--
			}
		}
	}

	for i > 0 {
		result = append(result, string(str1[i-1]))
		i--
	}
	for j > 0 {
		result = append(result, string(str2[j-1]))
		j--
	}
	fmt.Println(result)

	return reverse(result)

}
