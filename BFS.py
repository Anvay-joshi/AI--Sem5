def search(start, goal, search_space):
    open_list = [start]
    closed_list = []
    n = len(search_space)
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
            return True
        else:
            print("Goal test: False")
            children = search_space[n]
            for child in children:
                successors.append(child)
                if child not in closed_list and child not in open_list:
                    #open_list.insert(0,child)
                    open_list.append(child)
        print(f"Successors: {successors}\n")


def add_edge(search_space, u, v):
    if u not in search_space:
        search_space[u] = []
    if v not in search_space:
        search_space[v] = []
    search_space[u].append(v)
    search_space[v].append(u)
    
search_space = {}
add_edge(search_space, 'a', 'b')
add_edge(search_space, 'a', 'c')
add_edge(search_space, 'a', 'h')
add_edge(search_space, 'b', 'd')
add_edge(search_space, 'b', 'f')
add_edge(search_space, 'c', 'h')
add_edge(search_space, 'c', 'd')
add_edge(search_space, 'c', 'e')
add_edge(search_space, 'd', 'e')
add_edge(search_space, 'd', 'f')
add_edge(search_space, 'e', 'g')
add_edge(search_space, 'd', 'g')
add_edge(search_space, 'f', 'g')

print(search('a', 'g', search_space))
