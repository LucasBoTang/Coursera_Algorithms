def kosaraju(graph):
    """
    find all strongly connected components using Kosaraju’s algorithm
    """

    def dfs(u, graph, completed_order):
        """
        dfs with completed time tracking
        """
        stack = [u]
        # dfs with stack
        while stack:
            u = stack[-1]
            # explore u
            if u not in visited:
                visited.add(u)
                # add all unvisited adjacent vertex
                for v in graph[u]:
                    if v not in visited:
                        stack.append(v)
            else:
                # u is completed
                if u not in completed:
                    completed.add(u)
                    completed_order.append(u)
                stack.pop()
        return completed_order

    # reverse all arcs
    print("Reversing the graph...")
    graph_rev = reverse_graph(graph)

    # dfs completed time on reversed graph
    print("dfs on reversed graph...")
    # intialize
    visited = set()
    completed = set()
    order = []
    # go through all vertex
    for u in graph:
        if u not in visited:
            order = dfs(u, graph_rev, order)

    # dfs in descrsing order
    print("dfs on origanl graph...")
    sccs = []
    visited = set()
    completed = set()
    while order:
        u = order.pop()
        if u not in visited:
            # all visited vertex are in scc
            scc = dfs(u, graph, [])
            sccs.append(scc)

    return sccs


def reverse_graph(graph):
    """
    reverse directed graph
    """
    # intialize
    graph_rev = {}
    for u in graph:
        graph_rev[u] = []
    # add reversed edge v -> u
    for u in graph:
        for v in graph[u]:
            graph_rev[v].append(u)
    return graph_rev


def topk_size(lst, k):
    """
    get kth largest size
    """
    sizes = list(map(len, lst))
    sizes.sort()
    return sizes[::-1][:k]


# load txt as directed graph
graph = {}
for u in range(875714):
    graph[u+1] = []
print("Loading the text file...")
with open('./scc.txt', 'r') as f:
    for line in f:
        u, v = line.split()
        # add edge u -> v
        graph[int(u)].append(int(v))

# get all sccs
sccs = kosaraju(graph)

# 5 largest
res = topk_size(sccs, 5)
print("The size of 5th largest scc are as following:")
for i in res:
    print(i)
