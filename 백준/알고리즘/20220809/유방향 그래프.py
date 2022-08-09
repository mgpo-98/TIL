n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
graph2 = [[]for _ in range(n+1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    
    
    graph2[v1].append(v2)
    


print(graph)
print(graph2)