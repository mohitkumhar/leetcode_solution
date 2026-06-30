func maxIceCream(costs []int, coins int) int {
	slices.Sort(costs)
	var count = 0

	for _, cost := range costs {
		if (coins - cost) >= 0 {
			coins -= cost
			count += 1
		} else {
			break
		}
	}

	return count
}