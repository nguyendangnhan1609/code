test = int(input())
for i in range(test):
    n = int,input()
    s = input()
    s = s.replace('\n','')
    st = ""
    for x in s:
        if (x == 'L'):st += 'L'
        if (x == 'R'):st += 'R'
        if (x == 'D'):st += 'U'
        if (x == 'U'):st += 'D'
    print(st)