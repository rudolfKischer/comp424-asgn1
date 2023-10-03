from random import randint, sample, choice
from conflicts import update_queen

def get_random_queens(n):
    return [ randint(0, n-1) for _ in range(n) ]

def get_random_unique_queens(n):
    return sample(range(n), n)

def get_queens_spaced(n):
    r = 1
    queens = []
    for i in range(n):
        queens.append(r)
        r += 2
        if r >= n:
            r = 0
    return queens


class Queens():
    
    def __init__(self, n, max_steps=10000, queens=None):
        
        self.n = n
        self.queens = queens
        if queens is None:
            self.init_queens(n)
        self.build_conflicts()
        self.step = 0
        self.max_steps = max_steps

    def init_queens(self, n):
        new_queens = get_queens_spaced(n)
        self.queens = new_queens

    def diag_i(self, row, col):
        return row - col + self.n - 1
    
    def adiag_i(self, row, col):
        return row + col

    def build_conflicts(self):
        row_conflicts = [-1] * self.n
        diag_conflicts = [-1] * (2 * self.n - 1)
        anti_diag_conflicts = [-1] * (2 * self.n - 1)

        for (col, row) in enumerate(self.queens):
            row_conflicts[row] += 1
            diag_conflicts[self.diag_i(row,col)] += 1
            anti_diag_conflicts[self.adiag_i(row,col)] += 1
        

        queen_conflicts = [0] * self.n
        for (col, row) in enumerate(self.queens):
            queen_conflicts[col] = row_conflicts[row] + \
                diag_conflicts[self.diag_i(row,col)] + \
                anti_diag_conflicts[self.adiag_i(row,col)] 
            
        self.conflicts = queen_conflicts

    def get_queen_col_row_conflicts(self, queen_col):
        
        row_conflicts = [0] * self.n

        for (col, row) in enumerate(self.queens):
            if col == queen_col:
                continue
            # rows it conflicts with
            row_conflicts[row] += 1
            # diags it conflicts with
            # need to calculate the row , that the diag interceipts the column
            diag_row_t = row + queen_col - col
            if diag_row_t >= 0 and diag_row_t < self.n:
                row_conflicts[diag_row_t] += 1
            
            # anti diags it conflicts with
            anti_diag_row_t = row - queen_col + col
            if anti_diag_row_t >= 0 and anti_diag_row_t < self.n:
                row_conflicts[anti_diag_row_t] += 1
            
        return row_conflicts

    def get_min_conflict_row(self, queen_col):
        row_conflicts = self.get_queen_col_row_conflicts(queen_col)
        min_conf = min(row_conflicts)
        return choice([i for i, j in enumerate(row_conflicts) if j == min_conf]), min_conf
        
    def pick_queen(self):
        return choice([ i for i in range(self.n) if self.conflicts[i] > 0])
    
    def pick_row(self, queen_col):
        return self.get_min_conflict_row(queen_col)[0]
    
    def get_total_conflicts(self):
        return sum(self.conflicts)


    def improve_queens(self):
        queen_col = self.pick_queen()
        new_row = self.pick_row(queen_col)
        update_queen(self.n, self.conflicts, self.queens, queen_col, new_row)
    
    def solve_step(self):
        self.step += 1
        if self.step >= self.max_steps:
            print("max steps reached")
            return True
        if self.get_total_conflicts() == 0:
            return True
        self.improve_queens()
        return False
    

    def solve(self):
        print(f'Starting conflicts: {self.get_total_conflicts()}')
        while not self.solve_step():
            pass  
        return self.queens
        

    def display(self):
        for i in range(len(self.queens)):
            for j in range(len(self.queens)):
                full_square = "██"
                empty_square = "░░"
                if i == self.queens[j]:
                    print(".Q", end="")
                else:
                    if (i + j) % 2 == 0:
                        print(full_square, end="")
                    else:
                        print(empty_square, end="")
            print()
