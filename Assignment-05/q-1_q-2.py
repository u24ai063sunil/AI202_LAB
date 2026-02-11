def is_valid(g, b):
    # out of bounds
    if g < 0 or b < 0 or g > 3 or b > 3:
        return False

    # right bank people
    g_r = 3 - g
    b_r = 3 - b

    # left bank unsafe
    if g > 0 and b > g:
        return False

    # right bank unsafe
    if g_r > 0 and b_r > g_r:
        return False

    return True

moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def successors(state):
    g, b, boat = state
    next_states = []

    for mg, mb in moves:
        if boat == 0:  # boat on left → go right
            new = (g-mg, b-mb, 1)
        else:          # boat on right → go left
            new = (g+mg, b+mb, 0)

        if is_valid(new[0], new[1]):
            next_states.append(new)

    return next_states

# Depth-Limited Search
print("\nDepth-Limited Search:-")
explored_dls = 0

def DLS(state, goal, limit, path, visited):
    global explored_dls
    explored_dls += 1

    if state == goal:
        return path + [state]

    if limit == 0:
        return None

    visited.add(state)

    for child in successors(state):
        if child not in visited:
            result = DLS(child, goal, limit-1, path+[state], visited)
            if result:
                return result

    visited.remove(state)
    return None

start = (3,3,0)
goal = (0,0,1)
print("\nfor limit=3")
solution_dls = DLS(start, goal,3, [], set())

print("DLS Solution:", solution_dls)
print("States Explored (DLS):", explored_dls)
print("\nfor limit=10")
solution_dls = DLS(start, goal,10, [], set())

print("DLS Solution:", solution_dls)
print("States Explored (DLS):", explored_dls)
print("\nfor limit=15")
solution_dls = DLS(start, goal,15, [], set())

print("DLS Solution:", solution_dls)
print("States Explored (DLS):", explored_dls)

# Iterative Deepening Search
print("\nIterative Deepening Search:-")
def IDS(start, goal, max_depth=20):
    global explored_ids
    explored_ids = 0

    for depth in range(max_depth):
        visited=set()
        result = IDS_DLS(start, goal, depth, [], visited)
        if result:
            return result, depth

    return None, None


def IDS_DLS(state, goal, limit, path, visited):
    global explored_ids
    explored_ids += 1

    if state == goal:
        return path + [state]

    if limit == 0:
        return None

    visited.add(state)

    for child in successors(state):
        if child not in visited:
            result = IDS_DLS(child, goal, limit-1, path+[state], visited)
            if result:
                return result

    visited.remove(state)
    return None

solution_ids, depth = IDS(start, goal)

print("\nIDS Solution Path:")
for s in solution_ids:
    print(s)

print("Solution Depth:", depth)
print("States Explored (IDS):", explored_ids)
