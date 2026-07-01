func maximumSafenessFactor(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])
    neighbours := [][]int{
        {0,1}, {1,0}, {0,-1}, {-1,0},
    }

    dist := make([][]int, rows)

    for i := range dist {
        dist[i] = make([]int, cols)
    }

    queue := [][]int{}

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++{
            if grid[i][j] == 1 {
                dist[i][j] = 0
                queue = append(queue, []int{i, j})
            } else {
                dist[i][j] = -1
            }
        }
    }

    for len(queue) > 0 {
        cell := queue[0]
        x := cell[0]
        y := cell[1]

        queue = queue[1:]

        for _, nei := range neighbours {
            newX := x + nei[0]
            newY := y + nei[1]

            if 0 <= newX && newX < rows &&
               0 <= newY && newY < cols &&
               dist[newX][newY] == -1 {
                dist[newX][newY] = dist[x][y] + 1
                queue = append(queue, []int{newX, newY})
            }
        }
    }

    left := 0
    right := 401
    ans := 0

    for left < right {
        mid := left + (right - left) / 2
        
        queue := [][]int{}
        visited := make(map[[2]int]bool)

        if dist[0][0] >= mid {
            queue = append(queue, []int{0, 0})
            visited[[2]int {0,0}] = true

            for len(queue) > 0 {
                cell := queue[0]
                x := cell[0]
                y := cell[1]
                queue = queue[1:]

                if x == rows - 1 && y == cols - 1 {
                    ans = mid
                }

                for _, nei := range neighbours {
                    newX := x + nei[0]
                    newY := y + nei[1]

                    if newX >= 0 && newX < rows &&
                       newY >= 0 && newY < cols &&
                       ! visited[[2]int{newX, newY}] {
                            if dist[newX][newY] >= mid {
                                queue = append(queue, []int{newX, newY})
                                visited[[2]int {newX, newY}] = true
                            }
                       }    
                }
            }
        }

        if ans == mid {
            left = mid + 1
        } else {
            right = mid
        }
    }

    return ans
}