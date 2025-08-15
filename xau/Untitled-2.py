def khoi_tao(S):
    dict0 = {}
    for x in S:
        if dict0.get(x) == None: dict0[x] = 1
        else:
            dict0[x]+=1
    return dict0
import sys
# sys.stdin = open("ad.inp","r")
# sys.stdout = open("ad.out","w")
X=input(); Y=input()
dict1 = khoi_tao(X)
dict2 = khoi_tao(Y)
for x in dict1:
    if (dict2.get(x) != None):
        p1,p2 = dict1[x],dict2[x]
        dict1[x]-=min(p1,p2) 
        dict2[x]-=min(p1,p2)
res = 0
for x in dict1.values():
    res+=x;
for x in dict2.values():
    res+=x
print(res)