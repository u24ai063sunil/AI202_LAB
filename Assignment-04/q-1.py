cities = {
    0: "Chicago",
    1: "Detroit",
    2: "Cleveland",
    3: "Indianapolis",
    4: "Columbus",
    5: "Pittsburgh",
    6: "Buffalo",
    7: "Syracuse",
    8: "New York",
    9: "Philadelphia",
    10: "Baltimore",
    11: "Boston",
    12: "Providence",
    13: "Portland"
}

n = 14

# adjacency matrix
adj = [[0 for _ in range(n)] for _ in range(n)]

edges = [
    (0,1,283),(0,2,345),(0,3,182),
    (1,2,169),(1,6,256),
    (2,6,189),(2,5,134),(2,4,144),
    (3,4,176),
    (4,5,185),
    (5,6,215),(5,9,305),(5,10,247),
    (6,7,150),
    (7,8,254),(7,11,312),
    (8,9,97),(8,12,181),
    (9,10,101),(9,11,215),
    (11,12,50),(11,13,107)
]

for u, v, w in edges:
    adj[u][v] = w
    adj[v][u] = w


class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost


class PriorityQueue:
    def __init__(self, f):
        self.data = []
        self.f = f

    def add(self, node):
        self.data.append(node)
        self.data.sort(key=self.f)

    def pop(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0


class Problem:
    def __init__(self, initial, goal):
        self.INITIAL = initial
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal

    def ACTIONS(self, state):
        actions = []
        for i in range(n):
            if adj[state][i] != 0:
                actions.append(i)
        return actions

    def RESULT(self, state, action):
        return action

    def ACTION_COST(self, s, s_prime):
        return adj[s][s_prime]


def EXPAND(problem, node):
    children = []
    for action in problem.ACTIONS(node.state):
        cost = node.path_cost + problem.ACTION_COST(node.state, action)
        child = Node(action, node, cost)
        children.append(child)
    return children


def BeFS(problem, f):
    node = Node(problem.INITIAL)

    frontier = PriorityQueue(f)
    frontier.add(node)

    reached = {problem.INITIAL: node}
    explored = 0

    while not frontier.is_empty():
        node = frontier.pop()
        explored += 1

        if problem.is_goal(node.state):
            return node, explored

        for child in EXPAND(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)

    return None, explored


def f(node):
    return node.path_cost


def get_path(node):
    path = []
    while node:
        path.append(cities[node.state])
        node = node.parent
    return path[::-1]


# Driver code
start = 7   # Syracuse
goal = 0    # Chicago

problem = Problem(start, goal)
solution, explored_count = BeFS(problem, f)

print("Best First Search Path:")
print(get_path(solution))
print("Total cost:", solution.path_cost)
print("Number of paths explored:", explored_count)