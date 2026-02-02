class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state          
        self.parent = parent        
        self.action = action        
        self.path_cost = path_cost  
        
    def __repr__(self):
        return f"Node(state={self.state}, cost={self.path_cost})"
    
class Action:
    def __init__(self, from_state, to_state, cost):
        self.from_state = from_state
        self.to_state = to_state
        self.cost = cost

    def __repr__(self):
        return f"{self.from_state} -> {self.to_state} (cost={self.cost})"
    
class Actions:
    def __init__(self, graph):
        self.graph = graph

    def get_actions(self, state):
        actions = []
        for neighbor, cost in self.graph[state]:
            actions.append(Action(state, neighbor, cost))
        return actions
    
def result(state, action):
    return action.to_state

def expand(node, actions_obj):
    s = node.state  

    for action in actions_obj.get_actions(s):        
        s_prime = result(s, action)                  
        new_cost = node.path_cost + action.cost      

        child_node = Node(
            state=s_prime,
            parent=node,
            action=action,
            path_cost=new_cost
        )

        yield child_node

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, node, priority):
        self.queue.append((node, priority))

        self.queue.sort(key=lambda x: x[1])

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[0]

    def __repr__(self):
        return str([(n.state, p) for n, p in self.queue])

graph = {
    "Chicago": [("Detroit", 283), ("Indianapolis", 182), ("Cleveland", 345)],
    "Detroit": [("Chicago", 283), ("Cleveland", 169), ("Buffalo", 256)],
    "Indianapolis": [("Chicago", 182), ("Columbus", 176)],
    "Columbus": [("Indianapolis", 176), ("Cleveland", 144), ("Pittsburgh", 185)],
    "Cleveland": [("Chicago", 345), ("Detroit", 169), ("Columbus", 144), ("Pittsburgh", 134)],
    "Pittsburgh": [("Cleveland", 134), ("Columbus", 185), ("Buffalo", 215),
                   ("Philadelphia", 305), ("Baltimore", 247)],
    "Buffalo": [("Detroit", 256), ("Pittsburgh", 215), ("Syracuse", 150)],
    "Syracuse": [("Buffalo", 150), ("Boston", 312), ("New York", 254)],
    "New York": [("Syracuse", 254), ("Philadelphia", 97), ("Providence", 181)],
    "Philadelphia": [("New York", 97), ("Baltimore", 101)],
    "Baltimore": [("Philadelphia", 101), ("Pittsburgh", 247)],
    "Providence": [("New York", 181), ("Boston", 50)],
    "Boston": []
}

heuristic = {
    "Chicago": 983,
    "Detroit": 882,
    "Indianapolis": 900,
    "Columbus": 850,
    "Cleveland": 800,
    "Pittsburgh": 700,
    "Buffalo": 600,
    "Syracuse": 450,
    "New York": 215,
    "Philadelphia": 270,
    "Baltimore": 350,
    "Providence": 100,
    "Boston": 0
}

def reconstruct_path(node):
    path = []

    while node is not None:
        path.append(node.state)
        node = node.parent

    return path[::-1]


class BestFirstSearchAgent:
    def __init__(self, graph, goal_state, heuristic_table):
        self.graph = graph
        self.goal_state = goal_state
        self.heuristic = heuristic_table
        self.actions_obj = Actions(graph)

    def f(self, node):
        return self.heuristic[node.state]

    def search(self, start_state):
        start_node = Node(state=start_state)

        frontier = PriorityQueue()
        frontier.push(start_node, self.f(start_node))

        reached = {start_state: start_node}

        explored_count = 0

        while not frontier.is_empty():
            node = frontier.pop()
            explored_count += 1

            if node.state == self.goal_state:
                return node, explored_count

            for child in expand(node, self.actions_obj):
                s = child.state
                if s not in reached:
                    reached[s] = child
                    frontier.push(child, self.f(child))

        return None, explored_count

agent = BestFirstSearchAgent(
    graph=graph,
    goal_state="Boston",
    heuristic_table=heuristic
)

goal_node, explored = agent.search("Chicago")

print("Path Found:", " -> ".join(reconstruct_path(goal_node)))
print("Nodes Explored:", explored)
print("Total_cost:",goal_node.path_cost)