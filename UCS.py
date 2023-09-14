def printPath(start, goal, parent, search_space):
    path = [goal]
    cost = 0
    path_node = goal
    while(path_node != start):
        path_node = parent[path_node]
        path.append(path_node)
    path.reverse()
    print("\nPath: ", end = '')
    for i in path:
        print(i,end = " ")
        try:
            for edge in search_space[parent[i]]:
                if edge[0] == i:
                    cost += edge[1]
        except:
            cost += 0
    print(f"\nCost: {cost}\n")

def search(start, goal, search_space, parent):
    open_list = {start: 0}
    closed_list = []
    search_result = True
    while(len(open_list)):
        successors = []
        #open_list = sorted(open_list, key = lambda x: x[1])
        print(f"open list: {open_list}")

        n = min(open_list, key=lambda key: open_list[key])
        print(f"current: {n}")
        print(f"closed list: {closed_list}")
        del open_list[n]

        if not n in closed_list:
            closed_list.append(n)
        if(n == goal):
            print("Goal test: True")
            #return True
            search_result = True
            break
        else:
            print("Goal test: False")
            if(n not in search_space):
                print("Successors: \n")
                continue
            children = search_space[n]
            for child in children:
                successors.append(child)
                if not child[0] in closed_list:
                    if(child[0] not in open_list):
                        open_list[child[0]] = child[1]
                    else:
                        open_list[child[0]] = min(child[1], open_list[child[0]])
                    parent[child[0]] = n
        print(f"Successors: {successors}\n")
    if(search_result):
        printPath(start, goal, parent, search_space)



def add_edge(search_space, u, v, w):
    if u not in search_space:
        search_space[u] = []
    search_space[u].append([v, w])
    #parent[u] = -1
    #parent[v] = -1
    
search_space = {}
parent = {}

add_edge(search_space, 'S', 'D', 3)
add_edge(search_space, 'S', 'E', 9)
add_edge(search_space, 'S', 'P', 1)
add_edge(search_space, 'D', 'B', 1)
add_edge(search_space, 'D', 'C', 8)
add_edge(search_space, 'B', 'A', 2)
add_edge(search_space, 'C', 'A', 1)
add_edge(search_space, 'P', 'Q', 15)
add_edge(search_space, 'D', 'E', 2)
add_edge(search_space, 'H', 'P', 7)
add_edge(search_space, 'H', 'Q', 5)
add_edge(search_space, 'E', 'H', 8)
add_edge(search_space, 'E', 'R', 2)
add_edge(search_space, 'R', 'F', 1)
add_edge(search_space, 'F', 'G', 2)
add_edge(search_space, 'F', 'C', 3)

start = 'S'
goal = 'G'
search(start, goal, search_space, parent)
