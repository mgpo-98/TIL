t = int(input())
for i in range(1,t+1):
    li = list(map(int, input().split()))
    li.sort()
    if li[0]**2 + li[1]**2 == li[2]**2:
        print(f'Scenario #{i}:')
        print('yes\n')
    else :
        print(f'Scenario #{i}:')
        print('no\n')

