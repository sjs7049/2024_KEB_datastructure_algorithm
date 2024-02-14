graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]

def dfs(g, v, visited):
    visited[v] = True
    print(name_array[v], end=' ')
    for i in range(len(g)):
        if graph[v][i] == True and not visited[i]:
            dfs(g, i, visited)


name_array = ["문별", "솔라", "휘인", "쯔위", "선미", "화사"]
visited = [0 for _ in range(len(graph))]
print(f'방문 순서 ---> ', end='')
dfs(graph, 0, visited)