n = int(input())
player_list = []
result = []

for _ in range(n):
    a = input()
    player_list.append(a[0])
print(player_list)
first_names = set(player_list)
print(first_names)
for i in first_names:
    if player_list.count(i) >= 5:
        result.append(i)

if len(result) > 0:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")
