func solve(i, j int, s string, memo [][]int) bool {
	if i >= j {
		memo[i][j] = 1
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
		if ans == true {
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

func longestPalindrome(s string) string {
	n := len(s)
	max_pal := ""

	memo := make([][]int, n) // -1 -> not computed yet, 1 -> true, 0 -> false

	for i := 0; i < n; i++ {
		memo[i] = make([]int, n)
		for j := 0; j < n; j++ {
			memo[i][j] = -1
		}
	}

	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if solve(i, j, s, memo) {
				if (j - i + 1) > len(max_pal) {
					max_pal = s[i : j+1]
				}
			}
		}
	}

	return max_pal
}