func dfs(node int, matrix map[int][][]int, visited []bool) int{
    min_val := math.MaxInt

    if visited[node] == true{
        return 0
    }
    visited[node] = true

    for _, val := range matrix[node] {
        v := val[0]
        w := val[1]

        min_val = min(min_val, w)
        if !visited[v] {
            min_val = min(min_val, dfs(v, matrix, visited))
        }
    }
    return min_val
}

func minScore(n int, roads [][]int) int {
    
    matrix := make(map[int][][]int)

    for i := 0; i < len(roads); i++ {
        u := roads[i][0]
        v := roads[i][1]
        w := roads[i][2]

        matrix[u] = append(matrix[u], []int{v, w})
        matrix[v] = append(matrix[v], []int{u, w})
    }

    visited := make([]bool, n+1)
    min_val := dfs(1, matrix, visited)

    return min_val
}