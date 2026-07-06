import "container/heap"

type Node struct {
	cost int
	x    int
	y    int
}

type MinHeap []Node

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h MinHeap) Less(i, j int) bool {
	return h[i].cost < h[j].cost
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Node))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	last := old[n-1]
	*h = old[:n-1]
	return last
}

func findSafeWalk(grid [][]int, health int) bool {
	m := len(grid)
	n := len(grid[0])

	directions := [][]int{{1, 0}, {0, 1}, {0, -1}, {-1, 0}}
	distance := make([][]int, m)

	for i := 0; i < m; i++ {
		distance[i] = make([]int, n)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			distance[i][j] = math.MaxInt
		}
	}
	distance[0][0] = grid[0][0]

	hp := &MinHeap{}
	heap.Init(hp)

	heap.Push(hp, Node{distance[0][0], 0, 0})

	for hp.Len() > 0 {
		heapValue := heap.Pop(hp).(Node)
		curr_cost := heapValue.cost
		x := heapValue.x
		y := heapValue.y

		if curr_cost > distance[x][y] {
			continue
		}

		for _, direction := range directions {
			newX := x + direction[0]
			newY := y + direction[1]

			if 0 <= newX && newX < m &&
				0 <= newY && newY < n {
				new_dist := curr_cost + grid[newX][newY]

				if new_dist < distance[newX][newY] {
					distance[newX][newY] = new_dist
					heap.Push(hp, Node{new_dist, newX, newY})
				}
			}
		}
	}

	return (health - distance[m-1][n-1]) > 0
}