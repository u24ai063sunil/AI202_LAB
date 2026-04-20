class Queue:
    def __init__(self):
        self.data = []
        self.front = 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.data[self.front]
        self.front += 1
        return item

    def is_empty(self):
        return self.front >= len(self.data)


def forward_chaining_queue(rules, facts, goal):
    inferred = set()              
    agenda = Queue()              

    print("\nInitial Facts:", facts)

    for fact in facts:
        agenda.enqueue(fact)
        inferred.add(fact)

    while not agenda.is_empty():
        fact = agenda.dequeue()
        print(f"\nProcessing: {fact}")

        for premises, conclusion in rules:
            # If fact is part of premises
            if fact in premises:

                # Check if all premises are satisfied
                if set(premises).issubset(inferred):

                    if conclusion not in inferred:
                        print(f"Infer {conclusion} using {premises} -> {conclusion}")

                        inferred.add(conclusion)
                        agenda.enqueue(conclusion)

                        if conclusion == goal:
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

forward_chaining_queue(rules1a, facts1a, goal1a)


# 1(b)
rules1b = [
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D"),
    (["D", "E"], "F")
]
facts1b = ["A", "E"]
goal1b = "F"

forward_chaining_queue(rules1b, facts1b, goal1b)