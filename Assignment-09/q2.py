from collections import deque

graph = {
    'Syracuse': {'Buffalo': 150, 'Philadelphia': 253, 'New York': 254, 'Boston': 312},
    'Buffalo': {'Syracuse': 150, 'Detroit': 256, 'Cleveland': 189, 'Pittsburgh': 215},
    'Detroit': {'Buffalo': 256, 'Cleveland': 169, 'Chicago': 283},
    'Cleveland': {'Buffalo': 189, 'Detroit': 169, 'Chicago': 345, 'Columbus': 144, 'Pittsburgh': 134},
    'Pittsburgh': {'Buffalo': 215, 'Cleveland': 134, 'Columbus': 185, 'Philadelphia': 305, 'Baltimore': 247},
    'Philadelphia': {'Syracuse': 253, 'Pittsburgh': 305, 'New York': 97, 'Baltimore': 101},
    'New York': {'Syracuse': 254, 'Philadelphia': 97, 'Providence': 181, 'Boston': 215},
    'Columbus': {'Cleveland': 144, 'Pittsburgh': 185, 'Indianapolis': 176},
    'Indianapolis': {'Columbus': 176, 'Chicago': 182},
    'Chicago': {'Detroit': 283, 'Cleveland': 345, 'Indianapolis': 182},
    'Boston': {'Syracuse': 312, 'New York': 215, 'Portland': 107, 'Providence': 50},
    'Providence': {'Boston': 50, 'New York': 181},
    'Portland': {'Boston': 107},
    'Baltimore': {'Pittsburgh': 247, 'Philadelphia': 101}
}

start = "Syracuse"
goal = "Chicago"

#function to find the smallest path using BFS
def bfs_all_paths_costs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    results = []

    while queue:
        node, path, cost = queue.popleft()

        if node == goal:
            results.append((path, cost))

        for neighbor, w in graph[node].items():
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor], cost + w))

    return results


#function to find the smallest path using DFS
def dfs_all_paths_costs(graph, start, goal):
    stack = [(start, [start], 0)]
    results = []

    while stack:
        node, path, cost = stack.pop()

        if node == goal:
            results.append((path, cost))

        for neighbor, w in graph[node].items():
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor], cost + w))

    return results


# -------------------------------------------------------
# ALPHA-BETA PRUNING
# Parent node = MAX (wants to maximize edge cost)
# Child node  = MIN (wants to minimize edge cost)
# Levels alternate: even depth = MAX, odd depth = MIN
# -------------------------------------------------------

def alpha_beta_search(graph, start, goal):
    """Entry point — starts MAX turn at root."""
    result = {}
    value = max_value(graph, start, goal, visited=[start],
                      alpha=-float('inf'), beta=float('inf'),
                      depth=0, result=result)
    return value, result.get('path', []), result.get('pruned', [])


def max_value(graph, node, goal, visited, alpha, beta, depth, result):
    """MAX node: picks the neighbor with the HIGHEST edge cost."""
    if node == goal:
        if 'path' not in result:
            result['path'] = visited[:]
        return 0

    neighbors = [(nbr, w) for nbr, w in graph[node].items() if nbr not in visited]

    if not neighbors:
        return -float('inf')   # dead end, no value

    v = -float('inf')

    for i, (neighbor, w) in enumerate(neighbors):
        child_val = min_value(graph, neighbor, goal, visited + [neighbor],
                              alpha, beta, depth + 1, result)
        # edge cost + value returned from subtree
        combined = w + (child_val if child_val != -float('inf') else 0)

        if combined > v:
            v = combined

        if v > alpha:
            alpha = v

        # Beta cutoff
        if v >= beta:
            remaining = [nbr for nbr, _ in neighbors[i + 1:]]
            if remaining:
                result.setdefault('pruned', []).append({
                    'at_node'  : node,
                    'type'     : 'β-cutoff (MAX)',
                    'pruned'   : remaining,
                    'v'        : v,
                    'beta'     : beta
                })
            break

    return v


def min_value(graph, node, goal, visited, alpha, beta, depth, result):
    """MIN node: picks the neighbor with the LOWEST edge cost."""
    if node == goal:
        if 'path' not in result:
            result['path'] = visited[:]
        return 0

    neighbors = [(nbr, w) for nbr, w in graph[node].items() if nbr not in visited]

    if not neighbors:
        return float('inf')    # dead end, no value

    v = float('inf')

    for i, (neighbor, w) in enumerate(neighbors):
        child_val = max_value(graph, neighbor, goal, visited + [neighbor],
                              alpha, beta, depth + 1, result)
        combined = w + (child_val if child_val != float('inf') else 0)

        if combined < v:
            v = combined

        if v < beta:
            beta = v

        # Alpha cutoff
        if v <= alpha:
            remaining = [nbr for nbr, _ in neighbors[i + 1:]]
            if remaining:
                result.setdefault('pruned', []).append({
                    'at_node'  : node,
                    'type'     : 'α-cutoff (MIN)',
                    'pruned'   : remaining,
                    'v'        : v,
                    'alpha'    : alpha
                })
            break

    return v


#Run the code
bfs_results = bfs_all_paths_costs(graph, start, goal)
dfs_results = dfs_all_paths_costs(graph, start, goal)
ab_value, ab_path, ab_pruned = alpha_beta_search(graph, start, goal)

print("====== BFS Paths and Costs ======")
for p, c in bfs_results:
    print(p, " -> cost =", c)

print("\n====== DFS Paths and Costs ======")
for p, c in dfs_results:
    print(p, " -> cost =", c)

print("\n====== Alpha-Beta Pruning (MAX parent / MIN child) ======")
print("Path found :", ab_path)
print("Value      :", ab_value)

print("\n--- Pruned Nodes ---")
if ab_pruned:
    for entry in ab_pruned:
        if 'beta' in entry:
            print(f"  {entry['type']} at '{entry['at_node']}': "
                  f"pruned {entry['pruned']}  "
                  f"(v={entry['v']} >= β={entry['beta']})")
        else:
            print(f"  {entry['type']} at '{entry['at_node']}': "
                  f"pruned {entry['pruned']}  "
                  f"(v={entry['v']} <= α={entry['alpha']})")
else:
    print("  No nodes were pruned.")