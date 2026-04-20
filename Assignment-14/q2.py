# ───────────── BACKWARD CHAINING ─────────────

def backward_chaining(rules, facts, goal, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        print(f"{goal} is already known (fact)")
        return True

    if goal in visited:
        return False

    visited.add(goal)

    for premises, conclusion in rules:
        if conclusion == goal:
            print(f"Trying to prove {goal} using {premises} -> {goal}")

            if all(backward_chaining(rules, facts, p, visited) for p in premises):
                print(f"{goal} proven!")
                return True

    print(f"{goal} cannot be proven")
    return False


# ───────── TEST CASES ─────────

# 2(a)
rules2a = [
    (["P"], "Q"),
    (["R"], "Q"),
    (["A"], "P"),
    (["B"], "R")
]
facts2a = ["A", "B"]
goal2a = "Q"

print("\nBackward Chaining Result (2a):")
backward_chaining(rules2a, facts2a, goal2a)


# 2(b)
rules2b = [
    (["A"], "B"),
    (["B", "C"], "D"),
    (["E"], "C")
]
facts2b = ["A", "E"]
goal2b = "D"

print("\nBackward Chaining Result (2b):")
backward_chaining(rules2b, facts2b, goal2b)