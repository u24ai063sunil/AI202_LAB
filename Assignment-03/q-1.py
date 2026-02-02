# Type-1

# import random

# rooms = {'A': 'Dirt', 'B': 'Dirt', 'C': 'Dirt'}
# location = 'A'

# rule_table = {
#     ('A', 'Dirt'): ['Remove'],
#     ('A', 'No Dirt'): ['Move Right'],
#     ('B', 'Dirt'): ['Remove'],
#     ('B', 'No Dirt'): ['Move Left', 'Move Right'],
#     ('C', 'Dirt'): ['Remove'],
#     ('C', 'No Dirt'): ['Move Left']
# }

# def move(loc, action):
#     if loc == 'A' and action == 'Move Right': return 'B'
#     if loc == 'B' and action == 'Move Left': return 'A'
#     if loc == 'B' and action == 'Move Right': return 'C'
#     if loc == 'C' and action == 'Move Left': return 'B'
#     return loc

# print("Percept\t\tAction\t\tLocation")
# print("------------------------------------------")

# for _ in range(7):
#     status = rooms[location]
#     actions = rule_table[(location, status)]
#     action = random.choice(actions)

#     if(action=="Remove"):
#         print(f"({location},{status})\t{action}\t\t{location}")
#     else:
#         print(f"({location},{status})\t{action}\t{location}")

#     if action == 'Remove':
#         rooms[location] = 'No Dirt'
#     else:
#         location = move(location, action)

# Type-2 : user can give percepts
# import random

# def vacuum_agent(location, status):
#     if status == "Dirt":
#         return "Remove"

#     if location == "A":
#         return "Move Right"

#     if location == "C":
#         return "Move Left"

#     if location == "B":
#         return random.choice(["Move Left", "Move Right"])


# steps = int(input("Enter number of percepts: "))

# print("\nPercept\t\tAction")
# print("-------------------------------")

# for _ in range(steps):
#     location = input("Enter Location (A/B/C): ")
#     status = input("Enter Status (Dirt/No Dirt): ")

#     action = vacuum_agent(location, status)
#     print(f"({location}, {status})\t{action}")
# type-3
class Env:

    def __init__(self):
        self.cond = {
            "a": "dirty",
            "b": "dirty",
            "c": "dirty"
        }


class Agent:

    def __init__(self):
        self.loc = "a"
        self.cost = 0

        self.rule = {
            ("a", "dirty"): "vaccuum work",
            ("a", "clean"): "move right",
            ("b", "dirty"): "vaccuum work",
            ("b", "clean"): "move right",
            ("c", "dirty"): "vaccuum work",
            ("c", "clean"): "move left"
        }

        self.score = {
            "vaccuum work": 5,
            "move right": 1,
            "move left": 1,
            "no_op": 0
        }

    def next(self, curr, action):
        if action == "move right":
            if curr == "a":
                return "b"
            elif curr == "b":
                return "c"
            else:
                return "c"

        elif action == "move left":
            if curr == "c":
                return "b"
            elif curr == "b":
                return "a"
            else:
                return "a"

        return curr

    def act(self, env):

        status = env.cond[self.loc]
        percept = (self.loc, status)
        action = self.rule[percept]

        print(percept, "\t", action, "\t ", self.loc)

        if action == "vaccuum work":
            env.cond[self.loc] = "clean"
            self.cost += self.score[action]
        else:
            self.loc = self.next(self.loc, action)
            self.cost += self.score[action]

env = Env()
agent = Agent()

steps = 10

print("Percept\t\tAction\t\tLocation\tRoom Conditions")

for step in range(steps):
    agent.act(env)
    print("\t\t\t\t\t", env.cond)

print("\nTotal Cost:", agent.cost)