# 모음의 갯수 : a e i o u 
word ='apple'
cnt = 0 
mo = ['a','e','i','o','u']
for i in word:
    for j in mo:
        if i == j:
            cnt += 1

print(cnt)

#for char word :
    #if char in 'aeiou':
        #count +=1
#print(count)