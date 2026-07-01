func rob_house(nums []int) int {
    n := len(nums)
    dp := make([]int, n)

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for idx := 2; idx < n; idx++ {
        steal := nums[idx] + dp[idx - 2]
        skip := dp[idx - 1]

        dp[idx] = max(steal, skip)
    }

    return dp[n - 1]
}

func rob(nums []int) int {
    n := len(nums)

    if n == 1{
        return nums[0]
    } else if n == 2{
        return max(nums[0], nums[1])
    }

    a := rob_house(nums[1:])
    b := rob_house(nums[:n-1])

    return max(a, b)
}