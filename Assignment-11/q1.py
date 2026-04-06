"""
Gujarat District Map Coloring — Constraint Satisfaction Problem (CSP)
======================================================================
Goal: Color all districts so no two adjacent districts share the same color,
      using the MINIMUM number of colors (chromatic number).

Excluded (not districts): Diu, Rann of Kuchchh, Little Rann of Kuchchh

Algorithm: Backtracking CSP with:
  - MRV  (Minimum Remaining Values) heuristic
  - Degree heuristic (tie-breaker)
  - Forward Checking (arc consistency)
  - Iterative deepening over k = 2, 3, 4 … until a solution is found
"""

from collections import defaultdict
from typing import Optional

# ── 1. Adjacency list (symmetric) ────────────────────────────────────────────
# Based on the Gujarat map; edges represent shared borders.
ADJACENCY = {
    "Kuchchh":       ["Jamnagar", "Rajkot", "Surendranagar", "Patan", "Banaskantha"],
    "Banaskantha":   ["Kuchchh", "Patan", "Mehsana", "Sabarkantha"],
    "Patan":         ["Kuchchh", "Banaskantha", "Mehsana", "Surendranagar"],
    "Mehsana":       ["Banaskantha", "Patan", "Sabarkantha", "Gandhinagar", "Ahmedabad", "Surendranagar"],
    "Sabarkantha":   ["Banaskantha", "Mehsana", "Gandhinagar", "Kheda", "Panchmahal", "Dahod"],
    "Gandhinagar":   ["Mehsana", "Sabarkantha", "Ahmedabad"],
    "Ahmedabad":     ["Mehsana", "Gandhinagar", "Surendranagar", "Kheda", "Anand", "Botad"],
    "Surendranagar": ["Kuchchh", "Patan", "Mehsana", "Ahmedabad", "Botad", "Rajkot"],
    "Rajkot":        ["Kuchchh", "Surendranagar", "Botad", "Amreli", "Jamnagar"],
    "Jamnagar":      ["Kuchchh", "Rajkot", "Porbandar", "Devbhumi Dwarka"],
    "Devbhumi Dwarka": ["Jamnagar", "Porbandar"],
    "Porbandar":     ["Jamnagar", "Devbhumi Dwarka", "Junaghad"],
    "Junaghad":      ["Porbandar", "Amreli", "Gir Somnath", "Botad"],
    "Gir Somnath":   ["Junaghad", "Amreli"],
    "Amreli":        ["Rajkot", "Junaghad", "Gir Somnath", "Bhavnagar", "Botad"],
    "Botad":         ["Surendranagar", "Ahmedabad", "Anand", "Bhavnagar", "Amreli", "Rajkot"],
    "Bhavnagar":     ["Amreli", "Botad", "Anand", "Bharuch"],
    "Anand":         ["Ahmedabad", "Kheda", "Vadodara", "Bharuch", "Bhavnagar", "Botad"],
    "Kheda":         ["Ahmedabad", "Sabarkantha", "Gandhinagar", "Anand", "Vadodara", "Panchmahal"],
    "Panchmahal":    ["Sabarkantha", "Kheda", "Vadodara", "Dahod"],
    "Dahod":         ["Sabarkantha", "Panchmahal"],
    "Vadodara":      ["Kheda", "Anand", "Panchmahal", "Bharuch", "Narmada", "Chhota Udaipur"],
    "Chhota Udaipur":["Vadodara", "Narmada", "Panchmahal", "Dahod"],
    "Bharuch":       ["Bhavnagar", "Anand", "Vadodara", "Narmada", "Surat"],
    "Narmada":       ["Bharuch", "Vadodara", "Chhota Udaipur", "Surat"],
    "Surat":         ["Bharuch", "Narmada", "Tapi", "Navsari"],
    "Tapi":          ["Surat", "Narmada", "Dangs", "Navsari"],
    "Dangs":         ["Tapi", "Navsari"],
    "Navsari":       ["Surat", "Tapi", "Dangs", "Valsad"],
    "Valsad":        ["Navsari"],
}

# Make adjacency symmetric and build sorted district list
graph: dict[str, set[str]] = defaultdict(set)
for u, neighbors in ADJACENCY.items():
    for v in neighbors:
        graph[u].add(v)
        graph[v].add(u)

DISTRICTS = sorted(graph.keys())
N = len(DISTRICTS)


# ── 2. CSP Backtracking solver ────────────────────────────────────────────────

def select_unassigned(assignment: dict, domains: dict, graph: dict) -> Optional[str]:
    """MRV heuristic + Degree heuristic as tie-breaker."""
    unassigned = [d for d in DISTRICTS if d not in assignment]
    # MRV: fewest remaining colors
    min_remaining = min(len(domains[d]) for d in unassigned)
    candidates = [d for d in unassigned if len(domains[d]) == min_remaining]
    # Degree tie-breaker: most constrained neighbours
    return max(candidates, key=lambda d: len([n for n in graph[d] if n not in assignment]))


def forward_check(var: str, color: int, domains: dict, graph: dict) -> Optional[dict]:
    """Remove `color` from neighbours' domains; return None if any domain empties."""
    new_domains = {d: set(vals) for d, vals in domains.items()}
    for neighbor in graph[var]:
        if color in new_domains[neighbor]:
            new_domains[neighbor].discard(color)
            if not new_domains[neighbor]:
                return None          # domain wipe-out → prune
    return new_domains


def backtrack(assignment: dict, domains: dict, graph: dict, k: int) -> Optional[dict]:
    if len(assignment) == len(DISTRICTS):
        return assignment
    var = select_unassigned(assignment, domains, graph)
    for color in sorted(domains[var]):
        assignment[var] = color
        new_domains = forward_check(var, color, domains, graph)
        if new_domains is not None:
            new_domains[var] = {color}
            result = backtrack(assignment, new_domains, graph, k)
            if result is not None:
                return result
        del assignment[var]
    return None


def solve_min_colors(graph: dict, max_k: int = 6) -> tuple[int, dict]:
    """Iterate k = 2, 3, … until a valid coloring is found."""
    for k in range(2, max_k + 1):
        print(f"  Trying k = {k} colors …", end=" ")
        domains = {d: set(range(k)) for d in DISTRICTS}
        result = backtrack({}, domains, graph, k)
        if result is not None:
            print("✓ Solution found!")
            return k, result
        print("✗")
    raise RuntimeError("No solution found within max_k.")


# ── 3. Verify solution ────────────────────────────────────────────────────────

def verify(coloring: dict, graph: dict) -> bool:
    for u in graph:
        for v in graph[u]:
            if coloring[u] == coloring[v]:
                print(f"  CONFLICT: {u} and {v} both have color {coloring[u]}")
                return False
    return True


# ── 4. Pretty-print ───────────────────────────────────────────────────────────

COLOR_NAMES = {0: "Red", 1: "Blue", 2: "Green", 3: "Yellow", 4: "Purple", 5: "Orange"}
COLOR_EMOJI = {0: "🔴", 1: "🔵", 2: "🟢", 3: "🟡", 4: "🟣", 5: "🟠"}

def pretty_print(k: int, coloring: dict):
    print(f"\n{'='*60}")
    print(f"  Gujarat District Map Coloring  — {k} colors used")
    print(f"{'='*60}")
    # Group by color
    groups: dict[int, list] = defaultdict(list)
    for d, c in sorted(coloring.items()):
        groups[c].append(d)
    for c in sorted(groups):
        emoji = COLOR_EMOJI.get(c, "⬜")
        name  = COLOR_NAMES.get(c, f"Color-{c}")
        dists = ", ".join(groups[c])
        print(f"  {emoji} {name:8s} ({len(groups[c]):2d} districts): {dists}")
    print(f"\n  Total districts coloured: {len(coloring)}")
    print(f"  Chromatic number (min colors): {k}")


# ── 5. Main ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Gujarat Map Coloring CSP")
    print(f"Districts: {N}  |  Adjacency edges: {sum(len(v) for v in graph.values())//2}\n")
    print("Searching for minimum chromatic number via backtracking CSP …")
    k, coloring = solve_min_colors(graph)

    ok = verify(coloring, graph)
    print(f"\n  Constraint verification: {'PASSED ✓' if ok else 'FAILED ✗'}")

    pretty_print(k, coloring)

    # Also print raw assignment dict
    print(f"\n{'─'*60}")
    print("  Raw coloring (district → color index):")
    for d in sorted(coloring):
        c = coloring[d]
        print(f"    {d:<22s} → {COLOR_NAMES.get(c, c)} ({c})")