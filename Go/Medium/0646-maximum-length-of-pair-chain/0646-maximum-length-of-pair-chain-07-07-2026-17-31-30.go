func solve(idx int, prev int, n int, pairs [][]int, memo [][]int) int {
	if idx >= n {
		return 0
	}
	if memo[idx][prev + 1] != -1 {
		return memo[idx][prev + 1]
	}

	skip := solve(idx+1, prev, n, pairs, memo)

	take := skip
	if prev == -1 || pairs[prev][1] < pairs[idx][0] {
		take = 1 + solve(idx+1, idx, n, pairs, memo)
	}

	memo[idx][prev + 1] = max(take, skip)
	return memo[idx][prev + 1]
}

func findLongestChain(pairs [][]int) int {
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i][1] < pairs[j][1]
	})

	n := len(pairs)
	memo := make([][]int, n)

	for i := 0; i < n; i++ {
		memo[i] = make([]int, n)
		for j := 0; j < n; j++ {
			memo[i][j] = -1
		}
	}
	return solve(0, -1, n, pairs, memo)

}