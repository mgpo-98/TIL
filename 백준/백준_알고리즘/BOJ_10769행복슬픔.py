s = input()
ha = s.count(':-)')
sa = s.count(':-(')
if ha == sa:
    print('unsure')
elif ha > sa :
    print('happy')
elif ha < sa:
    print('sad')
elif sa == 0 and ha == 0:
    print('none')