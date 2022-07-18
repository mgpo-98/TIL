from cgitb import reset


word = 'banana'

result={}
for char in word:
    #딕셔너리에 키가 없다
    if not char in result:
        #키랑 값을 0으로 초기화
        result[char] = 0
    #딕셔너리에 키가 있다
    else: 
        result[char] += 1
print(result)
for key in result:
    print(key, reset[key])