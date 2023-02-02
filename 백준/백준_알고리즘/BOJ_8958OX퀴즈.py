n = int(input())
for _ in range(n):
    OX = list(input())
    score = 0
    s_score = 0
    for i in OX :
        if i == 'O':
            score += 1
            s_score += score
        else:
            score = 0
    print(s_score)
