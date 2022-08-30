from random import randrange
import sys
from tkinter import Y
sys.stdin = open('몬스터트럭.txt','r')
cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
r, c = map(int, input().split())
parking = []
for _ in range(r):
    parking.append(input())
for i in range(r):
    for j in range(c):
        if i +1 == r or j + 1 == c:
            break
        q = parking[i][j]
        y = parking[i+1][j]
        w = parking[i][j+1]
        z = parking[i+1][j+1]
        tmp = w+y+q+z
        if '#' in tmp :
            continue
        else :
            car = tmp.count('X')
            if car == 0:
                cnt0 +=1
            elif car == 1:
                cnt1 +=1
            elif car == 2:
                cnt2 += 1
            elif car == 3:
                cnt3 += 1
            elif car == 4:
                cnt4 += 1
print(cnt0)
print(cnt1)
print(cnt2)
print(cnt3)
print(cnt4)
