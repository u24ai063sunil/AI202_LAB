import random
import math

N = 8


# heuristic (number of conflicts)
def heuristic(board):
    conflicts = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                conflicts += 1
    return conflicts


# generate random board
def random_board():
    return [random.randint(0, N-1) for _ in range(N)]


# generate neighbors
def get_neighbors(board):
    neighbors = []
    for col in range(N):
        for row in range(N):
            if board[col] != row:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors


# -----------------------------
# FIRST CHOICE HILL CLIMBING
# -----------------------------
def first_choice_hill_climb(board):

    current = board
    steps = 0

    while True:

        current_h = heuristic(current)

        neighbors = get_neighbors(current)
        random.shuffle(neighbors)

        found = False

        for n in neighbors:
            if heuristic(n) < current_h:
                current = n
                steps += 1
                found = True
                break

        if not found:
            return current, steps


# -----------------------------
# RANDOM RESTART HILL CLIMBING
# -----------------------------
def hill_climb(board):

    current = board
    steps = 0

    while True:

        neighbors = get_neighbors(current)
        best = min(neighbors, key=heuristic)

        if heuristic(best) >= heuristic(current):
            return current, steps

        current = best
        steps += 1


def random_restart():

    total_steps = 0

    while True:

        board = random_board()
        result, steps = hill_climb(board)

        total_steps += steps

        if heuristic(result) == 0:
            return result, total_steps


# -----------------------------
# SIMULATED ANNEALING
# -----------------------------
def simulated_annealing(board):

    current = board
    steps = 0
    T = 100

    while T > 0.1:

        if heuristic(current) == 0:
            return current, steps

        neighbors = get_neighbors(current)
        next_state = random.choice(neighbors)

        delta = heuristic(current) - heuristic(next_state)

        if delta > 0:
            current = next_state
        else:
            prob = math.exp(delta / T)
            if random.random() < prob:
                current = next_state

        T *= 0.95
        steps += 1

    return current, steps


# -----------------------------
# RUN 50 EXPERIMENTS
# -----------------------------
def experiment(algorithm, name):

    print("\n", name)

    success = 0

    for i in range(50):

        board = random_board()

        initial_h = heuristic(board)

        if name == "Random Restart":
            final_board, steps = random_restart()
        else:
            final_board, steps = algorithm(board)

        final_h = heuristic(final_board)

        status = "Solved" if final_h == 0 else "Fail"

        if status == "Solved":
            success += 1

        print(i + 1, "   ","initial h :" ,initial_h, "      ","final h :", final_h, "     ","Steps :", steps, "   ", "result :" ,status)

    print("Success rate:", success, "/ 50")


# run experiments
experiment(first_choice_hill_climb, "First Choice")
experiment(random_restart, "Random Restart")
experiment(simulated_annealing, "Simulated Annealing")