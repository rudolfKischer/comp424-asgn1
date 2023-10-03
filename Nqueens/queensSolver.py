from queens import Queens
from threading import Thread
from queue import Queue
import threading

max_steps = 500000

class SolverThread(Thread):
    

    def __init__(self, n, solutions_queue, stop_event, thread_num, max_steps=100000):
        super().__init__()
        self.nqueens = Queens(n, max_steps=max_steps)
        self.solutions_queue = solutions_queue
        self.stop_event = stop_event
        self.max_steps = max_steps
        self.thread_num = thread_num

    
    def run(self):
        while not self.stop_event.is_set() and not self.nqueens.solve_step():
            pass

        self.solutions_queue.put(self.nqueens)

def nqueens_threaded(n, num_solvers=1):
    solutions_queue = Queue()
    solvers = []
    stop_event = threading.Event()
    for i in range(num_solvers):
        solver_thread = SolverThread(n, solutions_queue, stop_event, i, max_steps=max_steps)
        solver_thread.start()
        solvers.append(solver_thread)
    
    solution_nqueen = None
    try:
        solution_nqueen = solutions_queue.get()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    stop_event.set()
    for solver in solvers:
        solver.join()
    print(f'Finishing conflicts: {solution_nqueen.get_total_conflicts()}')
    return solution_nqueen.queens