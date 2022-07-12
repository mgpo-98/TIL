numbers =[0, 20, 100, 50]
max_num = 0 # 최소값이 0이라 마이너스 주의 따라서 max_num = numbers[0]으로 한다
# 반복
for n in numbers:
    print(n)
    # 만약 max값이 n보다 작으면 바꾼다
    if max_num<n:
        max_num =n
print(max_num)