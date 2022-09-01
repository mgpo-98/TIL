import imp
from random import randrange


import sys
sys.stdin = open('콘테스트.txt', 'r')
w = []
k = []
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))    
w.sort(reverse=True)
k.sort(reverse=True)
w_s = w[0] + w[1] + w[2]
k_s = k[0] + k[1] + k[2]
print(w_s, k_s)