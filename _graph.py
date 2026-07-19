graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print(graph)

for node in graph:
    print(node, "->", graph[node])
