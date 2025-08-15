import sys
# sys.stdin = open("WRITING.inp","r")
# sys.stdout = open("WRITING.out","w")
n,m=map(int, input().split())
X=input(); S=input()
dictX = {}
for i in X:
    if dictX.get(i)==None: dictX[i]=1
    else: dictX[i]+=1
dictS = {}
for i in range(n):
    if (dictS.get(S[i]) == None): dictS[S[i]]=1
    else: dictS[S[i]]+=1
kq = 0
if dictX==dictS: kq+=1
for i in range(n,m):
    if (dictS.get(S[i])==None): dictS[S[i]]=1
    else: dictS[S[i]]+=1
    dictS[S[i-n]]-=1
    if (dictS[S[i-n]]==0): dictS.pop(S[i-n])
    if (dictX == dictS): kq+=1
print(kq)