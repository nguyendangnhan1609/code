import sys
sys.stdin=open('nicestr.inp','r')
sys.stdout=open('nicestr.out','w')
s = input()
d1 = d2 = 0
for i in s:
    if i == 'a':d1 += 1
    else: d2 += 1
if d1!=d2:print(1)
else: print(2)
    