func solve(i, j int, s string, memo [][]bool) bool {
	if i >= j {
		return true
	}
    if memo[i][j] == true {
        return memo[i][j]
    }

	if s[i] == s[j] {
		memo[i][j] = solve(i+1, j-1, s, memo)
        return memo[i][j]
	} else {
		memo[i][j] = false
        return memo[i][j]
	}
}

func countSubstrings(s string) int {
	n := len(s)
	count := 0

    memo := make([][]bool, n)


    for i := 0; i < n; i++ {
        memo[i] = make([]bool, n)
        for j := 0; j < n; j++ {
            memo[i][j] = false
        }
    }

	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if solve(i, j, s, memo) {
				count++
			}
		}
	}

	return count
}