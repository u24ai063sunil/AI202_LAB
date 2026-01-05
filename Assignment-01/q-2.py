from collections import deque, defaultdict

# Graph from the given network

graph = defaultdict(list)

edges = [
    ("Rahul", "Neha1"),
    ("Rahul", "Sneha"),
    ("Rahul", "Arjun1"),
    ("Rahul", "Pooja1"),
    ("Rahul", "Maya"),

    ("Neha1", "Priya"),
    ("Neha1", "Aarav"),
    ("Neha1", "Akash"),

    ("Sneha", "Sunil"),

    ("Akash", "Sunil"),

    ("Sunil", "Raj"),
    ("Priya", "Raj"),

    ("Arjun1", "Neha2"),

    ("Pooja1", "Arjun2")
]

# build undirected graph
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

start = "Rahul"

# ----------------------------
# BFS TREE
# ----------------------------
def bfs_tree(graph, start):
    visited = set([start])
    queue = deque([start])
    tree_edges = []
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                tree_edges.append((node, neighbor))
                queue.append(neighbor)

    return order, tree_edges


# ----------------------------
# DFS TREE
# ----------------------------
def dfs_tree(graph, start):
    visited = set()
    stack = [start]
    tree_edges = []
    order = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            order.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    tree_edges.append((node, neighbor))
                    stack.append(neighbor)

    return order, tree_edges


# ----------------------------
# Run both
# ----------------------------
bfs_order, bfs_edges = bfs_tree(graph, start)
dfs_order, dfs_edges = dfs_tree(graph, start)

print("===== BFS Traversal Order =====")
print(bfs_order)

print("\n===== BFS Tree Edges =====")
for e in bfs_edges:
    print(e)

print("\n===== DFS Traversal Order =====")
print(dfs_order)

print("\n===== DFS Tree Edges =====")
for e in dfs_edges:
    print(e)

# output
# ===== BFS Traversal Order =====
# ['Rahul', 'Neha1', 'Sneha', 'Arjun1', 'Pooja1', 'Maya', 'Priya', 'Aarav', 'Akash', 'Sunil', 'Neha2', 'Arjun2', 'Raj']

# ===== BFS Tree Edges =====
# ('Rahul', 'Neha1')
# ('Rahul', 'Sneha')
# ('Rahul', 'Arjun1')
# ('Rahul', 'Pooja1')
# ('Rahul', 'Maya')
# ('Neha1', 'Priya')
# ('Neha1', 'Aarav')
# ('Neha1', 'Akash')
# ('Sneha', 'Sunil')
# ('Arjun1', 'Neha2')
# ('Pooja1', 'Arjun2')
# ('Priya', 'Raj')

# ===== DFS Traversal Order =====
# ['Rahul', 'Maya', 'Pooja1', 'Arjun2', 'Arjun1', 'Neha2', 'Sneha', 'Sunil', 'Raj', 'Priya', 'Neha1', 'Akash', 'Aarav']

# ===== DFS Tree Edges =====
# ('Rahul', 'Neha1')
# ('Rahul', 'Sneha')
# ('Rahul', 'Arjun1')
# ('Rahul', 'Pooja1')
# ('Rahul', 'Maya')
# ('Pooja1', 'Arjun2')
# ('Arjun1', 'Neha2')
# ('Sneha', 'Sunil')
# ('Sunil', 'Akash')
# ('Sunil', 'Raj')
# ('Raj', 'Priya')
# ('Priya', 'Neha1')
# ('Neha1', 'Aarav')
# ('Neha1', 'Akash')