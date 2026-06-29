func numOfStrings(patterns []string, word string) int {
    var count = 0

    for _, pattern := range patterns{
        if strings.Contains(word, pattern){
            count++
        }
    }

    return count
}