class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Arrays to keep track of used numbers in rows, cols, and 3x3 boxes
        # We use size 10 to easily index numbers 1 through 9.
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        boxes = [[False] * 10 for _ in range(9)]
        
        empty_cells = []
        
        # 1. Initialize the board state and record all empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = int(board[r][c])
                    box_index = (r // 3) * 3 + (c // 3)
                    
                    # Mark this number as used in its row, col, and box
                    rows[r][num] = True
                    cols[c][num] = True
                    boxes[box_index][num] = True

        def backtrack(index: int) -> bool:
            # If we've filled all empty cells, the board is solved
            if index == len(empty_cells):
                return True
            
            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)
            
            # Try placing digits 1 through 9
            for num in range(1, 10):
                # O(1) Check: Is it safe to place this number?
                if not rows[r][num] and not cols[c][num] and not boxes[box_index][num]:
                    
                    # Place the number and mark it as used
                    board[r][c] = str(num)
                    rows[r][num] = cols[c][num] = boxes[box_index][num] = True
                    
                    # Move to the next empty cell
                    if backtrack(index + 1):
                        return True
                        
                    # Backtrack: Undo the placement
                    board[r][c] = "."
                    rows[r][num] = cols[c][num] = boxes[box_index][num] = False
                    
            return False

        # Start backtracking from the first empty cell
        backtrack(0)