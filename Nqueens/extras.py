    # def sim_annealing_pick_queen(self):
    #     # pick the top queens with the most conflict
    #     # use the temperature overtime to pick a random queen
    #     # at the tempered step, we will pick the most conflicted queen
    #     # at the start, we will pick a random queen
    #     # in between, we will pick a random queen with a probability of the temperature
    #     # we will do this by sorting the queens by most conflicts
    #     # and then picking a random queen from the top n queens based on the temperature
    #     print(self.step)
    #     temperature = min((self.step / self.tempered_step), 1)
    #     print(temperature)
    #     queen_conflicts = self.conflicts.copy()
    #     queen_conflicts_enumerated = list(enumerate(queen_conflicts))
    #     #sort by conflicts
    #     queen_conflicts_enumerated.sort(key=lambda x: x[1], reverse=True)
    #     #pick a random queen from the top queens based on the temperature
    #     k = max(int(self.n * temperature), 1)
    #     top_k_queens = queen_conflicts_enumerated[:k]
    #     return choice(top_k_queens)[0]

    # def random_queen_with_conflict(self):
    #     # pick a random queen, as long as it has a conflict

    #     queens = list(enumerate(self.conflicts))
    #     queens.sort(key=lambda x: x[1], reverse=True)
    #     #remove queens with no conflicts
    #     queens = [i for i in queens if i[1] > 0]
    #     if len(queens) == 0:
    #         return 0
    #     return choice(queens)[0]


    # def get_top_k_queens(self, k):
    #     queen_conflicts = self.conflicts.copy()
    #     queen_conflicts_enumerated = list(enumerate(queen_conflicts))
    #     #sort by conflicts
    #     queen_conflicts_enumerated.sort(key=lambda x: x[1], reverse=True)
    #     return queen_conflicts_enumerated[:k]
    # def get_most_conflict_fixes_queen_top_k_queens(self):
    #     # do the same as above, but only consider the top n queens based on most conflicts
    #     # this will allow us to get a better solution faster
    #     percent =  1 - min((self.step % self.tempered_step) / self.tempered_step, 1.0)
    #     print(f'percent: {percent}')
    #     k = int(self.n * percent)
    #     k = min(k, 100)
    #     top_k_queens = self.get_top_k_queens(k)

    #     queen_conflict_fixes = [0] * self.n
    #     for i in top_k_queens:
    #         queen_conflict_fixes[i[0]] = self.conflicts[i[0]] - self.get_min_conflict_row(i[0])[1]
    #     return max(enumerate(queen_conflict_fixes), key=lambda x: x[1])[0]


    # def get_most_conflict_fixes_queen(self):
    #     queen_conflict_fixes = [0] * self.n
    #     for i in range(self.n):
    #         queen_conflict_fixes[i] = self.conflicts[i] - self.get_min_conflict_row(i)[1]
    #     return max(enumerate(queen_conflict_fixes), key=lambda x: x[1])[0]
    
    # def get_most_conflicts_queen(self):
    #     return max(enumerate(self.conflicts), key=lambda x: x[1])[0]