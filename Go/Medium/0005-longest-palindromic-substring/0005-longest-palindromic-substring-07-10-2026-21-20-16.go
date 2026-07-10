func check_pal(word string) bool {
	i := 0
	j := len(word) - 1

	for i < j {
		if word[i] != word[j] {
			return false
		} else {
			i++
			j--
		}
	}
	return true
}

func longestPalindrome(s string) string {
	n := len(s)
	max_pal := ""

	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if check_pal(s[i : j+1]) {
				if (j - i + 1) > len(max_pal) {
					max_pal = s[i : j+1]
				}
			}
		}
	}

	return max_pal
}