def printPath(start, goal, parent):
    path = [goal]
    path_node = goal
    while(path_node != start):
        path_node = parent[path_node]
        path.append(path_node)
    path.reverse()
    print("\nPath: ", end = '')
    for i in path:
        print(i,end = " ")
    print("\n")

def search(start, goal, search_space, parent):
    open_list = [start]
    closed_list = []
    search_result = False
    #n = len(search_space)
    while(len(open_list)):
        successors = []
        print(f"open list: {open_list}")
        n = open_list.pop(0)
        print(f"current: {n}")
        print(f"closed list: {closed_list}")
        if n not in closed_list:
            closed_list.append(n)
        if(n == goal):
            print("Goal test: True")
            search_result = True
            #return True
            break
        else:
            print("Goal test: False")
            children = search_space[n]
            for child in children:
                successors.append(child)
                if child not in closed_list and child not in open_list:
                    open_list.insert(0,child)
                    parent[child] = n
        print(f"Successors: {successors}\n")
    if(search_result):
        printPath(start, goal, parent)


def add_edge(search_space, u, v):
    if u not in search_space:
        search_space[u] = []
    if v not in search_space:
        search_space[v] = []
    search_space[u].append(v)
    search_space[v].append(u)
    #parent[u] = -1
    #parent[v] = -1
    
search_space = {}
parent = {}

add_edge(search_space, 'A', 'B')
add_edge(search_space, 'A', 'C')
add_edge(search_space, 'A', 'H')
add_edge(search_space, 'B', 'D')
add_edge(search_space, 'B', 'F')
add_edge(search_space, 'C', 'H')
add_edge(search_space, 'C', 'D')
add_edge(search_space, 'C', 'E')
add_edge(search_space, 'D', 'E')
add_edge(search_space, 'D', 'F')
add_edge(search_space, 'E', 'G')
add_edge(search_space, 'D', 'G')
add_edge(search_space, 'F', 'G')

start = 'H'
goal = 'F'
search(start, goal, search_space, parent)

