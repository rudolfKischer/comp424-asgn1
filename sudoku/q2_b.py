# 2x2 sudoku with backtracking
from colorama import Fore, Back, Style, init

init(autoreset=True)

sudoku_board = [0] * 16

####
# problem 1
#
# _ 1 _ _
# _ _ 1 _
# _ 4 _ 3
# _ 3 _ _

sudoku_board_p1 = [0, 1, 0, 0,
                    0, 0, 1, 0,
                    0, 4, 0, 3,
                    0, 3, 0, 0]

def row_is_valid(board, row, num):
      count = 0
      for i in range(4):
            if board[row*4 + i] == num:
                  count += 1
            if count > 1:
                  return False
      return True

def col_is_valid(board, col, num):
      count = 0
      for i in range(4):
            if board[col + i*4] == num:
                  count += 1
            if count > 1:
                  return False
      return True

def check_square(board, row, col, num):
    count = 0
    block_row_start = (row//2) * 2 
    block_col_start = (col//2) * 2

    for i in range(2):
        for j in range(2):
            if board[(block_row_start + i)*4 + block_col_start + j] == num:
                count += 1
            if count > 1:
                return False
    return True

def is_valid(board, row, col, num):
      return row_is_valid(board, row, num) and col_is_valid(board, col, num) and check_square(board, row, col, num)


def find_empty(board):
      for i in range(16):
            if board[i] == 0:
                  return i
      return -1

step = 0

def solve(board, depth=0, max_steps=None):
      global step
      if max_steps is not None and step >= max_steps:
            return True

      step += 1
      depth += 1


      empty = find_empty(board)
      if empty == -1:
            return True
      row = empty // 4
      col = empty % 4

      for i in range(1, 5):
            board[empty] = i
            if is_valid(board, row, col, i):
                  print(f"{step}. **Step [{step}] Depth [{depth}]**:")
                  print(f"Change: $({row}, {col}) \\rightarrow {i}$")
                  print_board_with_change(board, row, col)
                  print()
                  if solve(board, depth, max_steps):
                        return True
            board[empty] = 0
      
      print(f"Backtracking: ({row}, {col})")
      print()
      return False

def print_board(board):
      print(f'```')
      for i in range(4):
            for j in range(4):
                  print(board[i*4 + j], end = " ")
            print()
      print(f'```')

# def print_board_with_change(board, changed_row=None, changed_col=None):
#     changed_index = None
#     if changed_row is not None and changed_col is not None:
#         changed_index = changed_row * 4 + changed_col  # Adjusted for 4x4

#     for i in range(16):  # 4x4 board has 16 cells
#         if i == changed_index:
#             # Emphasize with a background color
#             print(Back.GREEN + str(board[i]), end=" ")
#         else:
#             print(board[i], end=" ")
        
#         if (i+1) % 4 == 0:  # Add newline after every four cells for 4x4 board
#             print(Back.RESET)


def print_board_with_change(board, changed_row=None, changed_col=None):
    changed_index = None
    if changed_row is not None and changed_col is not None:
        changed_index = changed_row * 4 + changed_col  # Adjusted for 4x4
    print(f'```')
    for i in range(16):  # 4x4 board has 16 cells
        if i == changed_index:
            # Emphasize with a background color
            print("\033[7m" + str(board[i]) + "\033[m", end=" ")
        else:
            print(board[i], end=" ")
        
        if (i+1) % 4 == 0:  # Add newline after every four cells for 4x4 board
            print(Back.RESET)
    print(f'```')

def main():
      print("# Problem:")
      print_board(sudoku_board_p1)
      print()
      print("### Step-by-Step Solution:")
      if solve(sudoku_board_p1, max_steps=10):
            print("### Final Solution:")
            print_board(sudoku_board_p1)
      else:
            print("No solution exists")


main()

        



