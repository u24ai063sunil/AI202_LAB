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
import random

def vacuum_agent(location, status):
    if status == "Dirt":
        return "Remove"

    if location == "A":
        return "Move Right"

    if location == "C":
        return "Move Left"

    if location == "B":
        return random.choice(["Move Left", "Move Right"])


steps = int(input("Enter number of percepts: "))

print("\nPercept\t\tAction")
print("-------------------------------")

for _ in range(steps):
    location = input("Enter Location (A/B/C): ")
    status = input("Enter Status (Dirt/No Dirt): ")

    action = vacuum_agent(location, status)
    print(f"({location}, {status})\t{action}")
