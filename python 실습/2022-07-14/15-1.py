
#1 리스트에 담는다
word ='banana'
result=[]
for idx in range(len(word)):
    if word[idx] == 'a':
        result.append(idx)
print(result)

#2 그때 그때 출력
# word = 'banana'
#result = []
# for idx in range(word):
    #if wrod[idx]=='a'
    #print(idx, end='')