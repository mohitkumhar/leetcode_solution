func solve(i int, j int, m int, n int, word1 string, word2 string, memo [][]int) int {
	if i == m {
		return n - j
	} else if j == n {
		return m - i
	} else if memo[i][j] != -1 {
		return memo[i][j]
	}

	result := 0
	if word1[i] == word2[j] {
		result += solve(i+1, j+1, m, n, word1, word2, memo)
	} else {
		result += 1 + min(solve(i, j+1, m, n, word1, word2, memo), solve(i+1, j, m, n, word1, word2, memo), solve(i+1, j+1, m, n, word1, word2, memo))
	}

	memo[i][j] = result
	return result
}

func minDistance(word1 string, word2 string) int {

	m := len(word1)
	n := len(word2)

	memo := make([][]int, m)
	for i := 0; i < m; i++ {
		memo[i] = make([]int, n)
		for j := 0; j < n; j++ {
			memo[i][j] = -1
		}
	}

	return solve(0, 0, m, n, word1, word2, memo)
}