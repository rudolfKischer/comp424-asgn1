from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def row_conflicts(queens, q1_col, q2_col):
    return queens[q1_col] == queens[q2_col]

def diag_conflicts(queens, q1_col, q2_col):
    return queens[q1_col] - q1_col == queens[q2_col] - q2_col

def anti_diag_conflicts(queens, q1_col, q2_col):
    return queens[q1_col] + q1_col == queens[q2_col] + q2_col

def conflict_count(queens, q1_col, q2_col):
    return row_conflicts(queens, q1_col, q2_col) + \
        diag_conflicts(queens, q1_col, q2_col) + \
        anti_diag_conflicts(queens, q1_col, q2_col)

def conflict(q1_row, q1_col, q2_row, q2_col):
    return row_conflicts(q1_row, q1_col, q2_row, q2_col) or \
        diag_conflicts(q1_row, q1_col, q2_row, q2_col) or \
        anti_diag_conflicts(q1_row, q1_col, q2_row, q2_col) 
    
def remove_queen(n, conflicts, queens, queen_col):
    for i in range(n):
        if i == queen_col:
            conflicts[i] = 0
            continue
        conflicts[i] -= conflict_count(queens, i, queen_col)

def add_queen(n, conflicts, queens, queen_col, new_row):
    queens[queen_col] = new_row
    for col in range(n):
        if col == queen_col:
            continue
        new_conflicts = conflict_count(queens, col, queen_col)
        conflicts[col] += new_conflicts
        conflicts[queen_col] += new_conflicts

def update_queen(n, conflicts, queens, queen_col, new_row):
    remove_queen(n, conflicts, queens, queen_col)
    add_queen(n, conflicts, queens, queen_col, new_row)