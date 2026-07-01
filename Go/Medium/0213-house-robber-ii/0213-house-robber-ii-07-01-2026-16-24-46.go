func rob_house(nums []int) int {
    n := len(nums)

    next_prev := nums[0]
    prev := max(nums[0], nums[1])
    ans := prev

    for idx := 2; idx < n; idx++ {
        steal := nums[idx] + next_prev
        skip := prev

        ans = max(steal, skip)

        next_prev = prev
        prev = ans

    }
    return ans
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