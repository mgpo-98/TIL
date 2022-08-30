import numbers
import sys

sys.stdin = open("1288_input.txt", "r")

n = int(input())

for i in range(1,n+1) :

    #input 가저오기
    N = int(input())
    #기록지
    numbers = set()
    while True:
    #while 반복 =>set 길이가 10이 될 때 까지
    # for 반복 :숫자를 문자로
            for n in str(N):
        numbers.add(n)
         # numbers set에 계속 추가.
            if len(numbers) == 10:
                N += N1
    print(f"#{i}",N)

            
    
