def is_safe(subject, color, graph, assignment):
    for neighbor in graph[subject]:
        if assignment.get(neighbor) == color:
            return False
    return True

def csp_coloring(graph, colors, subjects, assignment={}, index=0):
    if index == len(subjects):
        return assignment

    subject = subjects[index]
    for color in colors:
        if is_safe(subject, color, graph, assignment):
            assignment[subject] = color
            result = csp_coloring(graph, colors, subjects, assignment, index+1)
            if result:
                return result
            assignment.pop(subject)
    return None


# Example: 4 subjects with conflicts
graph = {
    "Math": ["Physics", "Chemistry"],
    "Physics": ["Math", "Biology"],
    "Chemistry": ["Math", "Biology"],
    "Biology": ["Physics", "Chemistry"]
}

colors = ["Slot1", "Slot2", "Slot3"]
subjects = list(graph.keys())

solution = csp_coloring(graph, colors, subjects)

print("Exam Timetable Assignment:")
for subject, slot in solution.items():
    print(f"{subject} -> {slot}")
