func countSubstrings(s string) int {
    n := len(s)
    dp := make([][]bool, n)
    count := 0

    for i := 0; i < n; i++ {
        dp[i] = make([]bool, n)
    }

    for L := 1; L <= n; L++ {
        for i := 0; L + i - 1 < n; i++ {
            j := L + i - 1

            if L == 1{
                dp[i][j] = true
            } else if L == 2 {
                dp[i][j] = s[i] == s[j]
            } else {
                dp[i][j] = s[i] == s[j] && dp[i + 1][j - 1] == true
            }
            if dp[i][j] == true {
                count++
            }
        }
    }

    return count
}