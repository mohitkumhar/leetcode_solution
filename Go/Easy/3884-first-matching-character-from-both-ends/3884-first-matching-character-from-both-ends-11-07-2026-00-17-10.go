func firstMatchingIndex(s string) int {
	var n = len(s)

	var i = 0
	var j = n - 1

	for i <= j {
		if s[i] == s[j] {
			return i
		}
		i++
		j--
	}
	return -1

}