from random import randrange


n = int(input())
m = int(input())
graph =[[]for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [False]*n

def dfs(start):
    cnt = 0
    stack= [start]
    visited[start]= True
    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                cnt += 1
                stack.append(adj)
    print(cnt)
                
dfs(1)

    