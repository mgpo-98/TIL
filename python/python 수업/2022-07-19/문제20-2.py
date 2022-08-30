from cgitb import reset
from unittest import result


number = 123
result = 0
while number:
    #몫은 다음 number 
    #나머지는 더해나간다
    result += number%10
    number //= 10
print(result)
