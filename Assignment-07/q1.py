import random
import math
import pandas as pd

N = 8
def random_board():
    return [random.randint(0,7) for _ in range(N)]

def heuristic(state):
    h = 0
    for i in range(N):
        for j in range(i+1, N):
            # same row
            if state[i] == state[j]:
                h += 1
            # same diagonal
            if abs(state[i]-state[j]) == abs(i-j):
                h += 1
    return h

def neighbours(state):
    neigh = []
    for col in range(N):
        for row in range(N):
            if row != state[col]:
                new_state = state.copy()
                new_state[col] = row
                neigh.append(new_state)
    return neigh

def steepest_hill_climbing(initial):
    current = initial
    steps = 0

    while True:
        h_current = heuristic(current)
        all_neigh = neighbours(current)

        best = current
        best_h = h_current

        for n in all_neigh:
            h = heuristic(n)
            if h < best_h:
                best = n
                best_h = h

        if best_h >= h_current:   # Local minimum
            return current, h_current, steps, False

        current = best
        steps += 1

        if best_h == 0:
            return current, 0, steps, True
        
results1 = []

for _ in range(50):
    board = random_board()
    init_h = heuristic(board)
    final, final_h, steps, solved = steepest_hill_climbing(board)

    results1.append([init_h, final_h, steps, solved])

df1 = pd.DataFrame(results1, columns=[
    "Initial h","Final h","Steps","Solved"
])

print(df1)
print("Solved:", df1["Solved"].sum(), "/ 50")