n, m = map(int, input().split())
na = [[]for _ in range(n+1)]
total = 0
for _ in range(m):
    v1, v2 = map(int, input().split())
    na[v1].append(v2)
    na[v2].append(v1)

visited = [False]*(n+1)
def dfs(start):
    stack = [start]
    visited[start] = True 
    while stack:
        cur = stack.pop()
        for adj in na[cur]:
            if not visited[adj]:
                visited[adj] =True
                stack.append(adj)
                dfs(1)
cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        cnt +=1
        dfs(i)
print(cnt)