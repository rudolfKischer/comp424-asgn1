from colorama import Fore, Back, Style, init




possible_val_board = [set(range(1, 5)) for _ in range(16)]

sudoku_board_p1 = [0, 1, 0, 0,
                    0, 0, 1, 0,
                    0, 4, 0, 3,
                    0, 3, 0, 0]

def remove(set, num):
      if num in set:
          set.remove(num)

def put(set, num):
      if num not in set:
          set.add(num)

def iter_row(row, num, put_or_remove):
      for i in range(4):
          put_or_remove(possible_val_board[row*4 + i], num)

def iter_col(col, num, put_or_remove):
      for i in range(4):
          put_or_remove(possible_val_board[col + i*4], num)

def iter_square(row, col, num, put_or_remove):
      block_row_start = (row//2) * 2 
      block_col_start = (col//2) * 2

      for i in range(2):
            for j in range(2):
                put_or_remove(possible_val_board[(block_row_start + i)*4 + block_col_start + j], num)

def put_num(row, col, num):
      iter_row(row, num, remove)
      iter_col(col, num, remove)
      iter_square(row, col, num, remove)

def remove_num(row, col, num):
      iter_row(row, num, put)
      iter_col(col, num, put)
      # iter_square(row, col, num, put)

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
      
      global possible_val_board

      step += 1
      depth += 1

      empty = find_empty(board)
      if empty == -1:
            return True
      row = empty // 4
      col = empty % 4

      possible_vals = list(possible_val_board[row*4 + col])

      if len(possible_vals) == 0:
            return False
      

      deep_copy_possible_val_board = [set(possible_val_board[i]) for i in range(16)]


      for i in possible_vals:
            board[empty] = i
            print()
            print(f"### {step}. Step [{step}] Depth [{depth}]: \n")
            display_possible_val_board()
            print(f"**Change**:[({row}, {col}) $\\rightarrow$ {i}] \n")
            print(f'**Possible Values for ({row},{col})**: {possible_vals} \n')
            print(f'**Attempting:** {i}')
            print_board_with_change(board, row, col)
            print()
            put_num(row, col, i)
            if solve(board, depth, max_steps):
                  return True
            print()
            possible_val_board = [set(deep_copy_possible_val_board[i]) for i in range(16)]
            board[empty] = 0
      
      print(f"Backtracking: ({row}, {col}) \n")
      
      return False

def init_possible_val_board(board):
      global possible_val_board
      possible_val_board = [set(range(1, 5)) for _ in range(16)]
      for i in range(16):
            if board[i] != 0:
                  put_num(i // 4, i % 4, board[i])


def print_board_with_change(board, changed_row=None, changed_col=None):
    changed_index = None
    if changed_row is not None and changed_col is not None:
        changed_index = changed_row * 4 + changed_col  # Adjusted for 4x4

    print('```')
    for i in range(16):  # 4x4 board has 16 cells
        if i == changed_index:
            # Emphasize with a background color
            print("[" + str(board[i]) + "]", end=" ")
        else:
            print(" " + str(board[i]) +  " ", end=" ")
        
        if (i+1) % 4 == 0:  # Add newline after every four cells for 4x4 board
            print("\n")
    print('```')

def print_board(board):
      for i in range(4):
            for j in range(4):
                  print(board[i*4 + j], end = " ")
            print()

def display_possible_val_board():
    cell_to_str = lambda cell: [
        str(i) if i in cell else "_" for i in range(1, 5)
    ]

    def print_cell(index):
        values = cell_to_str(possible_val_board[index])
        return [f"[{values[0]} {values[1]}]", f"[{values[2]} {values[3]}]"]
    print()
    print("### Possible Values Board:")
    print("```")
    for i in range(4):
        # Print the first line of each cell for this row
        for j in range(4):
            print(print_cell(4*i + j)[0], end=" ")
        print()
        
        # Print the second line of each cell for this row
        for j in range(4):
            print(print_cell(4*i + j)[1], end=" ")
        print()
        print()
    print("```")

     


def main():
      print('# Initial Board:')
      print('```')
      print_board(sudoku_board_p1)
      print('```')
      print("# Step by Step Solution")
      init_possible_val_board(sudoku_board_p1)
      print()
      solve(sudoku_board_p1, 0, 10)
      print('# Final Solution:')
      print_board_with_change(sudoku_board_p1)

main()


