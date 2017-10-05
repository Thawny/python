for i in range(0,100):
    if i % 3 and i % 5:                 # true --> i divisible NI pas 5 NI pas 3
        print(i, end=', ')
    elif not i % 3 and not i % 5:       # true --> i divisible par 3 ET par 5
        print('fizzbuzz', end=', ')
    elif not i % 3:                     # true --> i divisible par 3
        print('fizz', end=', ')
    elif not i % 5:                     # true --> i divisible par 5
        print('buzz', end=', ')
