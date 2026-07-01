func solve(idx int, nums []int, flag bool, memo [][]int) int {
    n := len(nums)

    f := 0
    if flag {
        f = 1
    }

    if idx >= n {
        return 0
    }else if memo[f][idx] != -1 {
        return memo[f][idx]
    }

    val := nums[idx]
    if flag {
        val = -val
    }

    take := val + solve(idx + 1, nums, ! flag, memo)
    skip := solve(idx + 1, nums, flag, memo)

    memo[f][idx] = max(take, skip)
    return memo[f][idx]
}

func maxAlternatingSum(nums []int) int64 {
    n := len(nums)
    memo := make([][]int, 2)

    for i, _ := range memo {
        memo[i] = make([]int, n)
        for j, _ := range memo[i] {
            memo[i][j] = -1
        }
    }

    return int64(solve(0, nums, false, memo))
}