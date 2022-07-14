word ='apple'
cnt = 0 
mo = ['a','e','i','o','u']
for i in word:
    for j in mo:
        if i == j:
            cnt += 1

print(cnt)
