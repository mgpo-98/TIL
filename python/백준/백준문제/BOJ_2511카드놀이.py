import sys

sys.stdin = open("2511카드놀이.txt", "r")

A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = 0
b = 0
win = 0
for i in range(10):
    if(A[i] > B[i]):
        a +=3
        win = 1
    elif(A[i] < B[i] ):
        b += 3
        win - 1
    else:
        a += 1
        b += 1
if ((a > b) or  (b == a and win == 1)):
    print('A')
elif ((a < b) or (b == a and win == -1)):
    print('B') 
else:
    print('D')       
