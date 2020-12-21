
graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}


def dfs_stack(graph, node):
    visited = [node]
    stack = [node]
    while stack:
        current_node = stack[-1]
        print("stack", stack)
        print("visited", visited)
        if current_node not in visited:
            visited.extend(current_node)
        remove_from_stack = True
        for next in graph[current_node]:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited

print (dfs_stack(graph1, 'A'))



