import "fmt"

func lengthOfLIS(nums []int) int {
	n := len(nums)
	LIS := make([]int, n)
    max_lis := 1

	for i := 0; i < n; i++ {
		LIS[i] = 1
	}

	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] {
				if (LIS[j] + 1) > LIS[i] {
					LIS[i] = LIS[j] + 1
                    max_lis = max(max_lis, LIS[i])
				}
			}
		}
	}

	return max_lis
}