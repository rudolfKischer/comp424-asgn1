

# Questions 3: N-Queens

## Part A:

#### Solution Decription

### General Approach
  - For this solution we start by placing N queens on the board. We know that there can only be one queen per column and one queen per Row. So we place N queens on the board each with a seperate column. 
  - We then check if this board is a solution. It probably won't be, so that means there are some queens that are attacking each other.
  - This means we will need to improve our solution. The way we are going to do this is by taking a queen that is currently being attacked and moving it to a new row. If this decreases the number of queens attacking each other, we will keep this new board. If not, we will try a different row for that queen.
  - We can repeat this process and overtime our board will have less and less conflicts until we have a solution.

---
### Heuristics:
  - We can increase the rate at which find a solution by choosing the queen and the row in a smarter way.
  
  - Possible Heuristics:
      - Pick a random queen that is being attacked O(n) or ~O(1)
      - Pick the queen with the most conflicts O(n)
      - Pick the row that minimize the number of conflicts O(n)
      - Pick the Queen that when moved minimizes the total number of conflicts O(N^2)
      - Pick randomly from the top k queens with the most conflicts O(n)
      - Pick a top k queens with the most conflicts and of these queens, pick the one that minimizes the total number of conflicts when moved to its best row O(n*k)
      - Simulated Annleaing: Pick randomly from the top K queens in conflict, but we decrease the size of k overtime by some factor.

  - Through a bit of experimentation I found that choosing a queen randomly that was being attacked or picking a queen that minimizes total conflicts from top k attacked queens performed quite well and minimized the number of conflicts quickly

  - I experiment with the other techniques like simulated annealing but found minimal improvement in time.

### Practical Implementation

  - Store the queens as an array of integers where the index is the column and the value is the row

  - Store the number of conflicts for each queen in an array of integers where the index is the column and the value is the number of conflicts

  - Can calculate if a set of queens are on the same diagonal by using the formula $|x_1 - x_2| = |y_1 - y_2|$ and anti diagonal by using the formula $x_1 + y_1 = x_2 + y_2$

  - Only build the conflict board once and then update it as we move queens around, this is much faster than recalculating the conflicts each time

  - To check which row has the least conflicts, instead moving the queen to each row and calculating the number of conflicts, we simply loop over each queen, and count which rows it conflicts with in the column were looking at. This means we can calculate the number of conflicts in O(n) time. Then we can simply pick the row with the least conflicts.

  -  **Trivial Starting Solution**: For any board that is an even sided, there is a usually a trivial solution. The placement of queens is similiar to placing them in a diagonal, but we add one extra space so they dont conflict. This Solves most even sided boards in O(n) time. We can also use this as a starting place for odd sided boards. Because it has a small number of conflicts, it will be solved quickly.

\newpage

## Part B:
#### Largest Solution

- NOTE: The trivial solution can work for a large percentage of boards of any size. For that reason, ther this algorithm will return solutions for very large N in a short amount of time. However I will only include the largest solution that was not solved by the trivial solution.

- NOTE: I will include the largest solution that can be found in a reasonable amount of time. I could have run this for half an hour for or longer for a larger solution but I feel like that gets away from the point of this exercise. For that reason I will only include the solutions I can find in less than 10s

- NOTE: To speed up computation this was run using pypy which compiles the python code to machine code. 



(See attached .txt file for full solution)
```
Starting conflicts: 17802
Finishing conflicts: 0
N: 26702, Time: 10.013225078582764
```
Solution
```
[1, 15719, 5, 7, 17999, ... 26694, 26696, 26698, 8959]
```


\newpage

## Part C:

#### Run Time Complexity


- It is a little hard to reason about the time complexity because it is a slightly randomized algorithm and the number of times we have to move a queen is varies alot. It is easier to reason about the time it takes to determine about which queen to move. We basically have three steps:
  - Pick a random queen without any conflicts O(n)
  - Calculate the number of conflicts for each row O(n)
  - Move the queen to the new row O(1)
  - Update the conflicts for all the queens based on the queen we just moved O(n)
- We can also consider the case that if every time we move a queen, we move it to a row with no conflicts, then we would have to repeat this process O(n) times worst case. In this case the overall time complexity would be O(n^2)

![graph| 400](runtime_graph.JPG){width=400px}

We can see here that it takes a parabolic shape so it is likely that the time complexity is O(n^2)

Notice that the graph is very jagged. This is because as mentioned earlier for some boards the trivial solution solves the problem virtually instantly.


\newpage

## Part D:

#### Local Optima

- For most hill climbing alorithms we have the problem of climbing to a local optima from which we can not improve by taking small steps.
- Originally I was using a heruristic that picked the queen with the most conflicts and moved it to the row that minimized the total number of conflicts. 

- This minimized the number of conflicts quickly but often got stuck in a local optima. To solve this I would do a random restart. This solved the problem but was very slow because we could find local optima very quickly and then may have to restart many times.

- Instead I decided on just picking a queen at  random that was being attacked and moving it to a row that minimized the number of conflicts. This was much faster and still minimized the number of conflicts quickly. Because we are picking a random queen its unlikely we end up just trying just picking the same queen over and over again. This means we are less likely to get stuck.


# Resources:

Many of the techniques used to speed up conflict detection were taken from [[(Click Me)this article]]( https://medium.com/@pranav.putta22/solving-n-queens-for-1-million-queens-with-minconflict-62ef798556e0) called "Solving N-Queens for 1 Million Queens with MinConflict" by Pranav Putta

The idea of using a trivial solution as the starting position for most boards was taken from a couple different sources:

- [(Click Me)Formal Verification of a Solution to the n-Queens Problem](https://ntrs.nasa.gov/api/citations/20200003161/downloads/20200003161.pdf)

- [(Click Me)Construction For the Solution to the M Eueens Problem](https://www.tandfonline.com/doi/abs/10.1080/0025570X.1969.11975924)
- [(Click Me)Finding First and Most Beutiful Queens](https://arxiv.org/pdf/1907.08246.pdf)

# Formatted Bibliography

- Fischetti, M., & Salvagnin, D. (2019). Finding First and Most-Beautiful Queens by Integer Programming. Department of Information Engineering, University of Padova, Italy. Retrieved from https://arxiv.org/pdf/1907.08246.pdf

- Hoffman, E. J., Loessi, J. C., & Moore, R. C. (1969). Constructions for the Solution of the m Queens Problem. Mathematics Magazine, 42(2), 66-72. https://doi.org/10.1080/0025570X.1969.11975924

- Malekpour, M. R. (2020). Formal Verification of a Solution to the n-Queens Problem (NASA/TM-2020-220588). Langley Research Center, Hampton, Virginia. Retrieved from https://ntrs.nasa.gov/api/citations/20200003161/downloads/20200003161.pdf

- Putta, P. (2022, February 3). Solving N-Queens for 1 Million Queens with MinConflict. Medium. Retrieved from https://medium.com/@pranav.putta22/solving-n-queens-for-1-million-queens-with-minconflict-62ef798556e0
