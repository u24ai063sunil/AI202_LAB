start_state = (
    7, 2, 4,
    5, 0, 6,
    8, 3, 1
)

goal_state = (
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
)

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    for move in moves[zero]:
        new_state = list(state)
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        neighbors.append(tuple(new_state))
    return neighbors

def bfs(start, goal):
    queue = [(start, 0)]   
    visited = set([start])
    explored = 0

    while queue:
        state, depth = queue.pop(0) 
        explored += 1

        if state == goal:
            return explored, depth

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))

    return explored, -1

def dfs(start, goal, depth_limit=50):
    stack = [(start, 0)]
    visited = set()
    explored = 0

    while stack:
        state, depth = stack.pop()  
        explored += 1

        if state == goal:
            return explored, depth

        if depth < depth_limit:
            visited.add(state)
            for neighbor in get_neighbors(state):
                if neighbor not in visited:
                    stack.append((neighbor, depth + 1))

    return explored, -1

bfs_explored, bfs_depth = bfs(start_state, goal_state)
dfs_explored, dfs_depth = dfs(start_state, goal_state)

print("BFS States Explored:", bfs_explored)
print("BFS Solution Depth:", bfs_depth)

print("DFS States Explored:", dfs_explored)
print("DFS Solution Depth:", dfs_depth)

# OUTPUT:-
# BFS States Explored: 169741
# BFS Solution Depth: 26
# DFS States Explored: 31304
# DFS States Explored: 31304
# DFS Solution Depth: 50