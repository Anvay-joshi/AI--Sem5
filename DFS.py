import sys
# Initialize an empty adjacency list
adjacency_list = {}

# Add edges to the adjacency list
def add_edge(adj_list, u, v):
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append(v)
    adj_list[v].append(u)

# Example: Adding edges
add_edge(adjacency_list, 1, 2)
add_edge(adjacency_list, 1, 3)
add_edge(adjacency_list, 1, 8)
add_edge(adjacency_list, 2, 4)
add_edge(adjacency_list, 2, 6)
add_edge(adjacency_list, 3, 8)
add_edge(adjacency_list, 3, 4)
add_edge(adjacency_list, 3, 5)
add_edge(adjacency_list, 4, 5)
add_edge(adjacency_list, 4, 7)
add_edge(adjacency_list, 4, 6)
add_edge(adjacency_list, 5, 7)
add_edge(adjacency_list, 6, 7)


# Print the adjacency list
print("Graph:\n")
for vertex, neighbors in adjacency_list.items():
    print(f"Vertex {vertex}: {neighbors}")


src = int(input("Enter source vertex:"))
if(src not in adjacency_list):
    print("invalid source")
    sys.exit()
dst = int(input("Enter destination vertex:"))
if(dst not in adjacency_list):
    print("invalid destination")
    sys.exit()

stack = []
visited = []
stack.append(src)
visited.append(src)
#curr_node

print("\npath from source node to destination node is:")
while(len(stack) != 0):
    curr_node = stack.pop()
    print(f"{curr_node}")
    if(curr_node == dst):
        break
    for v in adjacency_list[curr_node]:
        if(v not in visited):
            stack.append(v)







