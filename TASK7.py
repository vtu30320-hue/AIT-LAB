state = {
    "robot": "A",
    "cabinet": "B",
    "kit": "C",
    "unlocked": False,
    "has_kit": False
}

actions = []

# Goal: Get Kit

if state["robot"] != state["cabinet"]:
    actions.append("move(B)")
    state["robot"] = "B"

if not state["unlocked"]:
    actions.append("unlock_cabinet()")
    state["unlocked"] = True

if state["robot"] != state["kit"]:
    actions.append("move(C)")
    state["robot"] = "C"

if state["unlocked"] and state["robot"] == state["kit"]:
    actions.append("collect_kit()")
    state["has_kit"] = True

print("Action Sequence:")
for action in actions:
    print(action)

print("Goal Achieved:", state["has_kit"])