# t = int(input())
# sit = []
# a = list(map(int, input().split()))
# cnt = 0
# for i in range(3):
#     if a[i] in sit:
#         cnt +=1
#     else:
#         sit.append(a[i])
# print(cnt)

t = int(input())
a = list(map(int, input().split()))
s = len(list(set(a)))
print(t-s)