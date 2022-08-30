a = []
for i in range(3):
    a.append(int(input()))
if a[0] == a[1] == a[2] == 60:
    print('Equilateral')
elif (a[0] + a[1] + a[2] == 180) and (a[0] == a[1] or a[1] == a[2]  or a[0] == a[2]):
    print('Isosceles')
elif (a[0] + a[1] + a[2] == 180):
    print('Scalene')
else:
    print('Error')
