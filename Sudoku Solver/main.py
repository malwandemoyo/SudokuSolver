# Space left for gathering prerequisites for script modification (Delete me)
# All comments actually document everything
# Functions were not developed in order
# Order of development of functions:
    #Print board
    #Is Valid
    #Find Empty
    # Solve

# Chess position solver in the todo bucket 😉
##:wink::wink:


# Here place a sudoku puzzle as a list of lists
# A list is a horizontal line in sudoku
# Zeros Indicate a blank space
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Solving the puzzle
def solve(board):
    #print(board) # this can be uncommented if you want to see how the algorithm works
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    
    return False 

# Prints the board
# Was used as visualisation in the development of this Script
# Can be used to visualise unsolved puzzle, solved puzzle .solving the puzzle!?
def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i !=0:
            print("-----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j !=0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])         
            else:
                print(str(board[i][j]) + " ", end="")


# finding an empty square
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column
    
    return None

# Checks if the sequence is valid
# To be used in the solver function
def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column 
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3 ):
        for j in range(box_x * 3, (box_x*3) + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# Printing the Unsolved puzzle
print_board(board)
# Solving the puzzle (this can be visualized or not, depending on user's likes)
solve(board)
# Finally printing the solved board
print_board(board)


# 24 September,
# Work on the visualisation (PyQT5, tKinter or Pygame)
# Debugging and Unit Tests