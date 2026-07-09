func solve(i int, j int, m int, n int, text1 string, text2 string, memo [][]int) int {
	if i >= m || j >= n {
		return 0
	}
	result := 0

	if memo[i][j] != -1 {
		return memo[i][j]
	}

	if text1[i] == text2[j] {
		result += 1 + solve(i+1, j+1, m, n, text1, text2, memo)
	} else {
		result += max(solve(i+1, j, m, n, text1, text2, memo), solve(i, j+1, m, n, text1, text2, memo))
	}

	memo[i][j] = result
	return result

}

func longestCommonSubsequence(text1 string, text2 string) int {
	m := len(text1)
	n := len(text2)

	memo := make([][]int, m)

	for i := 0; i < m; i++ {
		memo[i] = make([]int, n)
		for j := 0; j < n; j++ {
			memo[i][j] = -1
		}
	}

	return solve(0, 0, m, n, text1, text2, memo)
}