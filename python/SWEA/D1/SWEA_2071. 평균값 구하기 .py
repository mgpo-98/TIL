t = int(input())
for i in range(1,t+1):
    li = list(map(int, input().split()))
    print(f'#{i} {round(sum(li)/len(li))}')
