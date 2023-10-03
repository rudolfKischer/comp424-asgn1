


# N Queens

Magic Bit Boards: https://www.youtube.com/watch?v=_vqlIPDR2TU

Bitwise N queens: https://medium.com/@shelldog42/solving-n-queens-with-bitwise-operators-6c5130d0c9c7

Leet Code N queens: https://www.youtube.com/watch?v=Ph95IHmRp5M

Min Queens (local search): https://medium.com/@carlosgonzalez_39141/using-ai-to-solve-the-n-queens-problem-2a5a9cc5c84c

- Local Search Approaches:
	- https://saturncloud.io/blog/fast-heuristic-algorithm-for-nqueens-problem-n-1000/
	- Min Constraints:
		- Start by placing a queen randomly 
		- Add the next queen that minimizes the number of constraints
		- repeat until we have place n queens
		- Completely restart if we stop seeing imporvements
	- Tabu Search:
		- Min Search but we keep a cache of arrangements we hae tried and failed
	- Min Constraints iterative fixes:
		- https://stackoverflow.com/questions/27697929/fast-heuristic-algorithm-for-n-queens-n-1000
		- Start by placing all queens in random position
		- pick a random queen , move it the the spot in that column that minimizes constraints
		- Alternatives:
			- Instead of just looking in the column look on the whole board (look in a smart way)
			- instead of just looking at one queen, look at all queens , and see which queen has the best move to do
			- Look multiple steps ahead, for each possible move, explore the next possible moves from there, and out of all the possible moves, pick the one that minimizes constraints
		- Min constraints with efficient row checking:
			- https://medium.com/@pranav.putta22/solving-n-queens-for-1-million-queens-with-minconflict-62ef798556e0
			- 
	- Simulated annealing:
		- Perform one of the local search methods, but dont always choose the best options
		- choose randomly from some percentage of the best options
		- Gradually overtime decrease the the range which you can randomly choose from
	- Monte Carlo Approach
		- for each possible move , run a monte carlo simulation
			- for each grandchild, of the children, choose k from the gran children, 
				- for the k grand children you have chosen, from there make m random moves
				- after each of these evaluate how many queens are still threated
				- This gives us an estimate for how good picking that child is
			- out of all of these children that now have a score
			- pick the child that has the best score


- Convert the python solution to a precompiled solution

N queens in linear time?: https://dergipark.org.tr/en/download/article-file/1184417


# Data structure Options

- Queens:
	- Queen array
		- we know there can only be one queen in each column
		- So we can make an array that is N long
		- each position represents a a queen
		- the number in the array represents what row the queen is on