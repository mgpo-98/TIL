while True:
    data = input()
    if data == '#' :
        break
    mo = ['a','e','i','o','u','A','E','I','O','U']
    res = 0
    for i in range(len(data)):
        if data[i] in mo :
            res += 1
    print(res)