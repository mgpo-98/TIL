while 1:
    li = list(map(int, input().split()))
    li.sort
    if li[0] == li[1] == li[2] == 0:
        break
    elif li[0] +li[1] <= li[2]:
        print('Invalid')
    elif li[0] == li[1] !=li[2] or li[0] == li[2] !=li[1] or li[1] == li[2] != li[0]:
        print('Isosceles')
    elif li[0] == li[1] == li[2]:
        print('Equilateral')
    else:
        print('Scalene')