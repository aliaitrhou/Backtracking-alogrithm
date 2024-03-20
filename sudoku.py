sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
]


# this function convert the boring list of list into a sudoku board schema.
def nice_visual(board):
    horizontal_line = "|-------+-------+-------|"
    for i in range(9):
        if i % 3 == 0:
            print(horizontal_line)
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")
            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")
            if j == 8:
                # this is for Adding a vertical bar at the end of each row
                print("|", end=" ")
        print()
    print(horizontal_line)


def possible(row, col, num):
    # this function take the coordinates of the specific box (num is the 9 possible numbers), then check to see
    # that the number (who has the  specific [row, col] coordinates) doesn't exist either in 3*3 box, row and col,
    # if so it return true else it return false (so we can use them in the main solve function).
    global sudoku_board
     # looping through rows
    for i in range(0, 9):
        if sudoku_board[row][i] == num:
            return False
     # looping through cols
    for i in range(0, 9):
        if sudoku_board[i][col] == num:
            return False
    # looping through 3*3 box
    x0 = (col//3)*3
    y0 = (row//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_board[y0 + i][x0 + j] == num:
                return False
    return True


print("board: ")
nice_visual(sudoku_board)


def solve():  # this function loop through the list of list, at the end of the board it uses the backtracking algorithm (Recursion) 
    #to raise up to the previous step if no solution found.
    global sudoku_board
    for y in range(9):
        for x in range(9):
            # that means that this specific 1*1 box is impty.
            if sudoku_board[y][x] == 0:
                # so we are gonna try all the 9 possible nums.
                for n in range(1, 10):
                    if possible(y, x, n):
                        sudoku_board[y][x] = n
                        solve()
                        sudoku_board[y][x] = 0
                return
    nice_visual(sudoku_board)


print("solutions: ")
solve()
