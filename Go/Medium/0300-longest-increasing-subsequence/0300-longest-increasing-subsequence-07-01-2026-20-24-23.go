func solve(idx int, prev int, nums []int, memo [][]int) int {
    n := len(nums)

    if idx >= n {
        return 0
    } else if memo[idx][prev + 1] != -1 {
        return memo[idx][prev + 1]
    }

    skip := solve(idx + 1, prev, nums, memo)
    
    take := skip
    if prev == -1 || nums[prev] < nums[idx] {
        take = 1 + solve(idx + 1, idx, nums, memo)
    }

    ans := max(take, skip)
    memo[idx][prev + 1] = ans

    return ans
}

func lengthOfLIS(nums []int) int {
    n := len(nums)

    memo := make([][]int, n)
    for idx, _ := range memo {
        memo[idx] = make([]int, n)
        for j, _ := range memo[idx] {
            memo[idx][j] = -1
        }
    }

    return solve(0, -1, nums, memo)

}