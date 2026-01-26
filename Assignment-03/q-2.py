# def railway_agent(percept):
#     emergency, train_in, train_out, obstacle = percept

#     if emergency == "Active":
#         return ("Lower", "On", "Red")

#     if obstacle == "Blocked":
#         return ("Lower", "On", "Red")

#     if train_in == "Detected" or train_out == "Detected":
#         return ("Lower", "On", "Green")

#     return ("Raise", "Off", "Green")

# test_cases = [
#     ("Neutral", "Detected", "Not Detected", "Clear"),
#     ("Neutral", "Not Detected", "Not Detected", "Blocked"),
#     ("Active", "Not Detected", "Not Detected", "Clear"),
#     ("Neutral", "Not Detected", "Not Detected", "Clear")
# ]

# print("Percept\t\t\t\t\t\t\tAction (Gate, Hooter, Signal)")
# print("-----------------------------------------------------------------------------------")

# for p in test_cases:
#     action = railway_agent(p)
#     print(f"{p}\t{action}")
# type-2
def railway_agent(emergency, train_in, train_out, obstacle):
    # Priority 1: Manual Emergency
    if emergency == "Active":
        return ("Lower", "On", "Red")

    # Priority 2: Obstacle on crossing
    if obstacle == "Blocked":
        return ("Lower", "On", "Red")

    # Priority 3: Train detected
    if train_in == "Detected" or train_out == "Detected":
        return ("Lower", "On", "Green")

    # Priority 4: Normal operation
    return ("Raise", "Off", "Green")


# -------- Simulation --------
steps = int(input("Enter number of percepts: "))

print("\nPercepts\t\t\t\tAction (Gate, Hooter, Signal)")
print("------------------------------------------------------------------")

for _ in range(steps):
    emergency = input("Manual Emergency (Active/Neutral): ")
    train_in = input("Train Inbound (Detected/NotDetected): ")
    train_out = input("Train Outbound (Detected/NotDetected): ")
    obstacle = input("Obstacle Sensor (Blocked/Clear): ")

    action = railway_agent(emergency, train_in, train_out, obstacle)

    print(f"({emergency}, {train_in}, {train_out}, {obstacle})\t{action}\n")
