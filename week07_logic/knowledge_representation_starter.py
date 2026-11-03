"""AINL3001 — Topic 7: Knowledge Representation and Logical Reasoning.

Student starter: complete the TODOs in Tasks 3 and 4.
This lab uses propositional facts and simple IF/THEN rules.

BSP
2026
"""

# TASK 1 — Represent facts (provided; inspect and experiment).
facts = {"rainy", "weekday"}

# TASK 2 — Represent rules (provided; inspect and experiment).
# Each rule is (list_of_required_facts, conclusion).
# All conditions must be known before the conclusion can be inferred.
rules = [
    (["rainy"], "take_umbrella"),
    (["rainy", "cold"], "wear_coat"),
    (["take_umbrella"], "stay_dry"),
]


def forward_chaining(known_facts, rules):
    """Return all original and inferred facts without changing known_facts.

    TASK 3 — TODO:
    1. Copy known_facts into a new set.
    2. Examine every rule and add its conclusion when ALL conditions hold.
    3. Repeat until an entire pass adds no new facts.
    4. Return the completed set.
    """
    # TODO

    inferred_facts = set(known_facts)

    new_fact_added = True

    while new_fact_added:

        new_fact_added = False

        for conditions, conclusion in rules:

            if all(condition in inferred_facts for condition in conditions):

                if conclusion not in inferred_facts:

                    inferred_facts.add(conclusion)

                    new_fact_added = True

    return inferred_facts

    pass


def query(inferred_facts, statement):
    """TASK 4 — Return True if statement is established in inferred_facts.

    A False result means 'not established', not necessarily 'false'.
    """
    # TODO
    
    return statement in inferred_facts

    pass


if __name__ == "__main__":
    print("=" * 55)
    print("TASK 0 — MANUAL REASONING")
    print("=" * 55)
    print("Initial facts:", sorted(facts))
    print("Rules:")
    for conditions, conclusion in rules:
        print(f"  IF {' AND '.join(conditions)} THEN {conclusion}")
    print("\nBefore coding, predict whether these can be inferred:")
    print("  take_umbrella?  stay_dry?  wear_coat?  Why?")
    print("\nAnswer: take_umbrella can be inferred because rainy must be true for take_umbrella, and rainy is a fact")
    print("\nAsnwer: stay_dry can be inferred because it uses take_umbrella which is a known fact based on if rainy THEN take umbrella")
    print("\nAnswer: wear_coat cant be inferred because while rainy is a known fact, it also needs cold, and cold is not a known fact so its false due to there not being enough information about cold")

    print("\n" + "=" * 55)
    print("TASKS 3–4 — FORWARD CHAINING AND QUERIES")
    print("=" * 55)
    inferred = forward_chaining(facts, rules)
    if inferred is None:
        print("Complete forward_chaining() to see inferred knowledge.")
    else:
        print("Initial facts:", sorted(facts))
        print("All known facts:", sorted(inferred))
        for statement in ("take_umbrella", "stay_dry", "wear_coat"):
            print(f"Can infer {statement}? {query(inferred, statement)}")

    print("\nTASK 5 — BACKWARD CHAINING (discussion)")
    print("Goal: stay_dry. Which rule concludes it? What must be true first?")
    print("\nAnswer: the rule IF take_umbrella THEN stay_dry concludes it. so take_umbrealla must be true first, and then take_umbrella comes from the known fact rainy, so stay_dry is proved")
    
    print("\nTASK 6 — LOGIC DISCUSSION")
    print("Is 'IF rainy THEN take_umbrella' always true in the real world?")
    print("\nAnswer: IF rainy then take umbrella is not always true in the real world because the real world has exceptions, not everyone has an umbrella or chooses to take on, in the program it is simply a rule based on the knowledge base")

    print("What assumptions does the rule make?")
    print("\nAnswer: the assumption this rule makes is that everyone must take an umbrealla if it rains")