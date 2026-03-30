import random


def is_goal(state):
    _, A, B=state
    return A=='C' and B=='C'


def actions():
    return ['SUCK', 'LEFT', 'RIGHT']


def results(state, action):
    location, A, B=state

    outcomes=[]

    if action=='SUCK':
        if location=='A':
            if A=='D':
                outcomes.append((location, 'C', B))
                outcomes.append((location, 'C', 'C'))
            else:
                outcomes.append((location, 'D', B))
                outcomes.append((location, A, B))

        elif location=='B':
            if B=='D':
                outcomes.append((location, A, 'C'))
                outcomes.append((location, 'C', 'C'))
            else:
                outcomes.append((location, A, 'D'))
                outcomes.append((location, A, B))

    elif action=='LEFT':
        if location=='B':
            outcomes.append(('A', A, B))
        else:
            outcomes.append(state)

    elif action=='RIGHT':
        if location=='A':
            outcomes.append(('B', A, B))
        else:
            outcomes.append(state)

    return outcomes


def and_or_search(state):
    return or_search(state, [])


def or_search(state, path):
    if is_goal(state):
        return []

    if state in path:
        return None  # avoid loops

    for action in actions():
        plan=and_search(results(state, action), path+[state])

        if plan is not None:
            return [action, plan]

    return None


def and_search(states, path):
    plans={}

    for s in states:
        plan=or_search(s, path)
        if plan is None:
            return None
        plans[s]=plan

    return plans


def print_plan(plan, indent=0):
    if plan==[]:
        print("  " * indent+"DONE")
        return
    if isinstance(plan, list):
        action=plan[0]
        print("  " * indent+f"Action: {action}")
        print_plan(plan[1], indent+1)

    elif isinstance(plan, dict):
        for state, subplan in plan.items():
            print("  " * indent+f"If state={state}:")
            print_plan(subplan, indent+1)

    else:
        print("  " * indent+"DONE")


def main():
    tiles=['A','B']
    state=['C','D']
    initial_state=(tiles[random.randint(0,1)], state[random.randint(0,1)], state[random.randint(0,1)])
    print("Initial State:", initial_state)
    plan=and_or_search(initial_state)

    if plan:
        print("Solution Plan:\n")
        print_plan(plan)
    else:
        print("No solution found.")


if __name__=="__main__":
    main()