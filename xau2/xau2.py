# import sys
# sys.stdin = open("STRDEL.INP","r")
# sys.stdout = open("STRDEL.OUT","w")
t = int(input())
for i in range(t):
    S=input()
    d=0
    for j in S:
        if (j=='A'): d+=1
        else:
            d-=1
            if d<0: d=1
    print(d)