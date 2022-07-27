m = list(map(int, input().split()))
res =[1, 2, 3, 4, 5, 6, 7, 8]
if m == res:
    print('ascending')
elif m == res[::-1]:
    print('descending')
else :
    print('mixed')
