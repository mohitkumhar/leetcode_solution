func sumAndMultiply(n int) int64 {
	s := strconv.Itoa(n)
	x := ""
	sum := 0

	for _, char := range s {
        if char != '0' {
            x += string(char)
            sum += int(char - '0')
		}
	}

    if x == "" {
        return 0
    }

    num, _ := strconv.Atoi(x)

    return int64(num * sum)
}