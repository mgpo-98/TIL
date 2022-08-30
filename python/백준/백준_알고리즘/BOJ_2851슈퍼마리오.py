
s = 0
a = 0
for i in range(10):
    n = int(input())
    s += n
    if 100-a >= abs(100-s): # = 을 넣어야 절댓값이 같을 시 최대 총점 출력이 가능
        a = s
print(a)
