func largestDivisibleSubset(nums []int) []int {
	sort.Ints(nums)
    n := len(nums)
	dp := make([]int, n+1)
	prev_idx := make([]int, n+1)
    count := 0
	max_seen_idx := -1

	for i := 0; i <= n; i++ {
		dp[i] = 1
		prev_idx[i] = -1
	}

	fmt.Println(dp)
	fmt.Println(prev_idx)

	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
            if nums[i] % nums[j] == 0 {
                if dp[i] < (dp[j] + 1) {
                    dp[i] = dp[j] + 1
                    prev_idx[i] = j
                }
            }
		}
        if dp[i] > count {
            count = dp[i]
            max_seen_idx = i
        }
	}

    result := make([]int, 0)

    for max_seen_idx != -1 {
        result = append(result, nums[max_seen_idx])
        max_seen_idx = prev_idx[max_seen_idx]
    }

	return result
}