# ───────────── RESOLUTION METHOD ─────────────

def negate(literal):
    return literal[1:] if literal.startswith("~") else "~" + literal


def resolve(ci, cj):
    resolvents = []
    for di in ci:
        for dj in cj:
            if di == negate(dj):
                new_clause = list(set(ci + cj))
                new_clause.remove(di)
                new_clause.remove(dj)
                resolvents.append(new_clause)
    return resolvents


def resolution(kb, query):
    clauses = kb + [[negate(query)]]

    print("\nInitial Clauses:")
    for c in clauses:
        print(c)

    while True:
        new = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = resolve(clauses[i], clauses[j])

                for r in resolvents:
                    print(f"Resolving {clauses[i]} and {clauses[j]} -> {r}")
                    if not r:
                        print("\nDerived EMPTY clause ⇒ PROVED")
                        return True
                    new.append(r)

        if all(r in clauses for r in new):
            print("\nNo new clauses ⇒ NOT PROVED")
            return False

        clauses.extend(new)


# ───────── TEST CASES ─────────

# 3(a)
kb3a = [
    ["P", "Q"],     # P ∨ Q
    ["~P", "R"],    # P → R
    ["~Q", "S"],    # Q → S
    ["~R", "S"]     # R → S
]
query3a = "S"

resolution(kb3a, query3a)


# 3(b)
kb3b = [
    ["~P", "Q"],
    ["~Q", "R"],
    ["S", "~R"],
    ["P"]
]
query3b = "S"

resolution(kb3b, query3b)