def search(start, goal, search_space):
    open_list = {start: 0}
    closed_list = []
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
            return True
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
        print(f"Successors: {successors}\n")


                    



def add_edge(search_space, u, v, w):
    if u not in search_space:
        search_space[u] = []
    search_space[u].append([v, w])
    
search_space = {}

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

print(search('S', 'G', search_space))
