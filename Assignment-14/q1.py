# ───────────── FORWARD CHAINING ─────────────

def forward_chaining(rules, facts, goal):
    inferred = set(facts)
    print("\nInitial Facts:", inferred)

    while True:
        new_inferred = set()

        for premises, conclusion in rules:
            if set(premises).issubset(inferred) and conclusion not in inferred:
                print(f"Infer {conclusion} using {premises} -> {conclusion}")
                new_inferred.add(conclusion)

        if not new_inferred:
            break

        inferred.update(new_inferred)

        if goal in inferred:
            print(f"\nGoal {goal} reached!")
            return True

    print(f"\nGoal {goal} NOT reached.")
    return False


# ───────── TEST CASES ─────────

# 1(a)
rules1a = [
    (["P"], "Q"),
    (["L", "M"], "P"),
    (["A", "B"], "L")
]
facts1a = ["A", "B", "M"]
goal1a = "Q"

forward_chaining(rules1a, facts1a, goal1a)


# 1(b)
rules1b = [
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D"),
    (["D", "E"], "F")
]
facts1b = ["A", "E"]
goal1b = "F"

forward_chaining(rules1b, facts1b, goal1b)