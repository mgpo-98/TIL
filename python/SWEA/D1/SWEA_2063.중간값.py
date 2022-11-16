n = int(input())
data = list(map(int, input().split()))

data.sort()
len_value = n // 2
print(data[len_value])
