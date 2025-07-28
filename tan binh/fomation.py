n,m=map(int, input().split())
L=[0]*(n+3);R=[0]*(n+3)
#Khoi tao L,R
for i in range(1,n+1):
    L[i]=i-1
    R[i]=i+1
L[1]=0;R[1]=n+1
R[0]=1;L[n+1]=1 
for i in range(1,m+1):
    a=list(map(int,input().split()))
    if a[0]==1: #chen a1 ben trai a2
        R[L[a[2]]]=a[1]
        L[a[1]]=L[a[2]]
        R[a[1]]=a[2]
        L[a[2]]=a[1]
    if a[0]==2:#chen a1 ben phai a2
        R[a[2]]=a[1]
        L[a[1]]=a[2]
        R[a[1]]=R[a[2]]
        L[R[a[2]]]=a[1]
    if a[0]==3:#xoa a1
        R[L[a[1]]]=R[a[1]]
        L[R[a[1]]]=L[a[1]]
    if a[0]==4:#hien thi La1,Ra1
        print(L[a[1]],R[a[1]])