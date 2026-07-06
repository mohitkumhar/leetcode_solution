import "sort"
func removeCoveredIntervals(intervals [][]int) int {

    sort.Slice(intervals, func(i, j int) bool {
        start1 := intervals[i][0]
        end1 := intervals[i][1]

        start2 := intervals[j][0]
        end2 := intervals[j][1]

        if start1 != start2 {
            return start1 < start2
        }
        return end1 > end2
    })

    max_end := 0
    ans := 0

    for _, interval := range intervals {
        fmt.Println(interval)
        end := interval[1]

        if end > max_end {
            max_end = end
            ans += 1
        }
    }
    return ans

}