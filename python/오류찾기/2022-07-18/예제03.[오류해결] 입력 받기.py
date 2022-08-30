# numbers = int(input().split())
# print(sum(numbers))

numbers = map(int, input().split())
print(sum(numbers))
#오류 이유 : 타입 에러로 map을 이용해 int 삽입으로 오류 해결

