#문자로 순회하는 것이 아니라!
#인덱스로 접근해서 쓰자
#원하는 숫자? 0, ,1 ,2 ,3
#얻는 방법? range(len(word)) =>range(6)=>0~5
word ='banana'
cnt = 0 
ind = -1
for i in word:
    if i == 'a':
        ind = cnt
        break
    cnt +=1
    
print(ind)


# word
# for idx in range(len(word)):
        #print(idx,word[idx])
    #if word[idx] =='a':
        #print(idx)
        #break
#else :
 #   print(-1)
