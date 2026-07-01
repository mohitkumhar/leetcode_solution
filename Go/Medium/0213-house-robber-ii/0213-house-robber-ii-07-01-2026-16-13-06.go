func rob_house(i int, nums []int, memo []int) int {
    n := len(nums)
    if i >= n {
        return 0
    }

    if memo[i] != -1 {
        return memo[i]
    }

    steal := nums[i] + rob_house(i + 2, nums, memo) 
    skip := rob_house(i + 1, nums, memo)

    memo[i] = max(steal, skip)
    return memo[i]
}

func rob(nums []int) int {
    n := len(nums)

    if n == 1{
        return nums[0]
    } else if n == 2{
        return max(nums[0], nums[1])
    }

    memo1 := make([]int, n)
    for idx, _ := range memo1 {
        memo1[idx] = -1
    }

    memo2 := make([]int, n)
    for idx, _ := range memo2 {
        memo2[idx] = -1
    }

    a := rob_house(0, nums[1:], memo1)
    b := rob_house(0, nums[:n-1], memo2)

    return max(a, b)
}