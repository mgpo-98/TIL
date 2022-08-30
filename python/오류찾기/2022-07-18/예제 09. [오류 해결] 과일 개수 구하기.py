from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        # fruit_count = {fruit: 1} 오류코드
        fruit_count[fruit] = 1 #딕셔너리의 키를 지정 해서 값을 넣어줘야한다.
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)



# fruit_count = {fruit: 1} 오류코드
# 위와 같이 작성하면 딕셔너리의 목록이 모두 새로 추가되지 않고 
# 처음 항목만 추가된다.
# 그러므로 
# fruit_count[fruit] = 1
# 이렇게 작성해 딕셔커리의 키를 지정해서 값을 넣어줘야한다.

# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)