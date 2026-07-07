type Item struct {
	dist int
	node int
}
type MinHeap []Item

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	return h[i].dist < h[j].dist
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	last := old[n-1]
	*h = old[:n-1]
	return last
}

func dj(mid_ans int, n int, k int64, matrix map[int][]Edge) bool {
	distance := make([]int, n)
	for i := 0; i < n; i++ {
		distance[i] = math.MaxInt
	}

	distance[0] = 0

	hp := &MinHeap{}
	heap.Init(hp)
	heap.Push(hp, Item{0, 0})

	for hp.Len() > 0 {
		curr_node := heap.Pop(hp).(Item)
		curr_dist := curr_node.dist
		node := curr_node.node

		if curr_dist > int(k) {
			return false
		}
		if node == n-1 {
			return true
		}
		if curr_dist > distance[node] {
			continue
		}

		for _, nei_node := range matrix[node] {
			if nei_node.w < mid_ans {
				continue
			}
			newDist := curr_dist + nei_node.w
			if newDist < distance[nei_node.v] {
				distance[nei_node.v] = newDist
				heap.Push(hp, Item{newDist, nei_node.v})
			}
		}
	}
	return false
}

type Edge struct {
	v int
	w int
}

func findMaxPathScore(edges [][]int, online []bool, k int64) int {
	n := len(online)
	matrix := make(map[int][]Edge)

	for _, edge := range edges {
		u, v, w := edge[0], edge[1], edge[2]
		if online[u] && online[v] {
			matrix[u] = append(matrix[u], Edge{v, w})
		}
	}

	left := 0
	right := int(1e9)
	ans := -1

	for left <= right {
		mid := left + (right-left)/2

		if dj(mid, n, k, matrix) {
			ans = mid
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return int(ans)
}