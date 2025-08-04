n,k,s = input().split()
n = int(n); k =int(k)
L = [0]*(n+3)
R = [0]*(n+3)
for i in range(1,n+1):
    L[i]=i-1
    R[i]=i+1
L[1]=0;R[n]=n+1
R[0]=1;L[n+1]=1
for x in s:
    if x =='.':break;
    if x =='A':p=R[0]
    else:p=R[R[0]]
    R[L[p]]=R[p]
    L[R[p]]=L[p]
    R[L[m+1]]=p
    L[p]=L[m+1]
    R[p]=m+1
    L[m+1]=p
p=R[0]
for i in range(1,k+1):p=R[p]
print(L[p]-1,p-1,R[p]-1)