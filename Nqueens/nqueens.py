from time import time
# import matplotlib.pyplot as plt
from queens import Queens
import csv
from queensSolver import nqueens_threaded

        
max_steps = 500000

def n_queens(n):
    nqueen = Queens(n, max_steps=max_steps)
    nqueen.solve()
    if n <= 100:
        # nqueen.display()
        pass
    print(f'Finishing conflicts: {nqueen.get_total_conflicts()}')
    return nqueen.queens

def solve_n_queens(n):
    start = time()
    # solution = nqueens_threaded(n, 4)
    solution = n_queens(n)
    if n > 500:
        print(f'Solution: {solution[:10]} ... {solution[-10:]}')
    end = time()
    print(f'N: {n}, Time: {end - start}')
    return end - start
    
    
def test(n_max, n_min=8, test_step_size=1):
    # run the nquens for all sizes up to n starting at 8
    # store the time it take
    # plot the results as a function of n

    times = {}
    for i in range(n_min, n_max + 1, test_step_size):
        times[i - n_min] = solve_n_queens(i)
    
    with open('runtimes_table.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['n', 'time'])
        for n, time in times.items():
            writer.writerow([n, time])

def main():
    n = 1000000
    start = time()
    test(n, 10, 500)
    end = time()
    print(f'Total Time: {end - start}')
    

if __name__ == "__main__":
    main()