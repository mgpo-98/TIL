
from importlib.resources import read_binary
import sys

sys.stdin = open("7785회사사람.txt", "r")
n = int(input())
dic = {}

for i in range(n):
    n,m = map(str, input().split())
    if m =='enter' : 
        dic[n] ='enter'
    else:
        del dic[n]
dic =sorted(dic.keys(),reverse=True)
for n in dic:
    print(n)

