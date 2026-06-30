func numberOfSubstrings(s string) int {
	n := len(s)
	var count = 0
	var left = 0
	freq := make(map[byte]int)

	for right := 0; right < n; right++ {

		freq[s[right]]++

		for len(freq) == 3 {
			count += n - right

			freq[s[left]]--
			if freq[s[left]] == 0 {
				delete(freq, s[left])
			}
			left++
		}
	}

	return count
}