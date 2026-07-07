func findLongestChain(pairs [][]int) int {
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i][1] < pairs[j][1]
	})

	prev_end := -1001
    curr_front := 0
    count := 0

	for _, pair := range pairs {
        
        curr_front = pair[0]

        if prev_end < curr_front {
            count++
            prev_end = pair[1]
        }
	}

    return count
}