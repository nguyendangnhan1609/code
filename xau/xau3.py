
chuyen = d = 0
n = int(input())
s = input()
for x in s:
    if (x == '('):
        d +=1
    else:
        d -=1
    if d<0:
        chuyen +=1
        d = 0
print(chuyen)