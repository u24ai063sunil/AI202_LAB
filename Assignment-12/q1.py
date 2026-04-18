from collections import deque

# ── Domain & Conflict Setup ────────────────────────────────────────────────────

ROOMS = {"R1", "R2", "R3"}

CONFLICTS = {
    "P1": ["P2", "P3", "P6"],
    "P2": ["P1", "P3", "P4"],
    "P3": ["P1", "P2", "P5"],
    "P4": ["P2", "P6"],
    "P5": ["P3", "P6"],
    "P6": ["P1", "P4", "P5"],
}

def initial_domains():
    return {team: set(ROOMS) for team in CONFLICTS}

def constraint(val_i, val_j):
    """Two conflicting teams must be in different rooms."""
    return val_i != val_j

# ── AC-3 ──────────────────────────────────────────────────────────────────────

def ac3(domains):
    """
    Apply AC-3 to the CSP.
    Returns (arc_consistent: bool, final_domains: dict).
    Prints a trace of every arc check.
    """
    # Initialise queue with every directed arc (Xi, Xj) for each conflict
    queue = deque()
    for xi, neighbors in CONFLICTS.items():
        for xj in neighbors:
            queue.append((xi, xj))

    arc_num = 0

    while queue:
        xi, xj = queue.popleft()
        arc_num += 1
        revised, removed = revise(domains, xi, xj)

        status = f"removed {removed}" if removed else "no change"
        print(f"  Arc {arc_num:>2}: ({xi} → {xj})  {status}")

        if revised:
            if not domains[xi]:          # domain wiped out → failure
                print(f"\n  ✗ Domain of {xi} is empty — AC-3 detects FAILURE.\n")
                return False, domains
            # Re-add arcs into Xi from all its other neighbors
            for xk in CONFLICTS[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    print()
    return True, domains


def revise(domains, xi, xj):
    """
    Remove values from domains[xi] that have no support in domains[xj].
    Returns (revised: bool, removed_values: set).
    """
    removed = set()
    for val_i in set(domains[xi]):
        # Check if ANY value in xj satisfies the constraint
        if not any(constraint(val_i, val_j) for val_j in domains[xj]):
            domains[xi].remove(val_i)
            removed.add(val_i)
    return bool(removed), removed


# ── Pretty Printer ─────────────────────────────────────────────────────────────

def print_domains(domains, title="Domains"):
    print(f"\n  {title}:")
    for team, dom in sorted(domains.items()):
        bar = ", ".join(sorted(dom)) if dom else "∅  ← EMPTY"
        print(f"    {team}: {{{bar}}}")
    print()


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  AC-3  |  Tech-Hub Meeting-Room Scheduling CSP")
    print("=" * 60)

    # ── Part 1: Plain AC-3 (no pre-assignment) ────────────────────────────────
    print("\n[ Part 1 ]  AC-3 without any pre-assignment\n")
    domains = initial_domains()
    print_domains(domains, "Initial domains")

    print("  Arc-reduction trace:")
    consistent, domains = ac3(domains)
    print_domains(domains, "Domains after AC-3")

    if consistent:
        all_full = all(len(d) == 3 for d in domains.values())
        print("  Result: arc-consistent ✓")
        if all_full:
            print("  Note : No domain was reduced — the constraint graph")
            print("         is satisfiable with 3 rooms, but a backtracking")
            print("         search is still needed to find a valid assignment.\n")

    # ── Part 2: Pre-assign P1 = R1, then run AC-3 ────────────────────────────
    print("=" * 60)
    print("\n[ Part 2 ]  Pre-assign P1 = R1, then run AC-3\n")
    domains2 = initial_domains()
    domains2["P1"] = {"R1"}           # force assignment
    print_domains(domains2, "Domains after P1 = R1")

    print("  Arc-reduction trace:")
    consistent2, domains2 = ac3(domains2)
    print_domains(domains2, "Domains after AC-3 (with P1 = R1)")

    if consistent2:
        print("  Result: AC-3 detects NO failure ✓")
        print("  Reduced domains are still valid — search can continue.\n")
    else:
        print("  Result: AC-3 detected a FAILURE ✗\n")


if __name__ == "__main__":
    main()