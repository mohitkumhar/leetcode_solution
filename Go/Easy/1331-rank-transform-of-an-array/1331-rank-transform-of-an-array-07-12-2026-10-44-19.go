func arrayRankTransform(arr []int) []int {
	set := make(map[int]bool)

	for _, num := range arr {
		set[num] = true
	}

	sortedArr := make([]int, 0, len(set))
	for key, val := range set {
		if val {
			sortedArr = append(sortedArr, key)
		}
	}

	sort.Ints(sortedArr)
	rankMap := make(map[int]int)
	rank := 1

	for _, num := range sortedArr {
		rankMap[num] = rank
		rank++
	}

	result := make([]int, len(arr))
	for i, num := range arr {
		result[i] = rankMap[num]
	}

	return result
}