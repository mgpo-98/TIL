n, m = map(int, input().split())

j = int(input())

ap = []

for _ in range(j):
    ap.append(int(input()))

move = 0
end = m
start = 1

for i in range(j):
    if end >= ap[i] and start <= ap[i]:
        continue
    elif end < ap[i]:
        move += ap[i] - end
        end = ap[i]
        start = ap[i] - (m - 1)

    elif start > ap[i]:
        move += start - ap[i]
        start = ap[i]
        end = ap[i] + (m - 1)
print(move)
