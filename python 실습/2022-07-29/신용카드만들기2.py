import sys

sys.stdin = open("input.txt", "r")

t = int(input())
a = ['3','4','5','6','9']
for po in range(1,t+1):
    c = input()
    card = c.replace('-','')  # '-' 제거 
    res = 0
    if (card[0] in a) and (len(card) == 16):  # a속에 있는 숫자가 맨앞에있고 숫자가 16개면 1출력
        res = 1
    else:
        res = 0
    print(f'#{po} {res}')