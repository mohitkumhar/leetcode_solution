func solve(i, j int, s string, memo [][]int) bool {
	if i >= j {
		return true
	}
	if memo[i][j] != -1 {
		if memo[i][j] == 1 {
            return true
        } else {
            return false
        }
	}

	if s[i] == s[j] {
		ans := solve(i+1, j-1, s, memo)
		if ans == true{
            memo[i][j] = 1
        } else {
            memo[i][j] = 0
        }
        return ans

	} else {
		memo[i][j] = 0
		return false
	}
}

func countSubstrings(s string) int {
	n := len(s)
	count := 0

	memo := make([][]int, n)

	for i := 0; i < n; i++ {
		memo[i] = make([]int, n)
		for j := 0; j < n; j++ {
			memo[i][j] = -1
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