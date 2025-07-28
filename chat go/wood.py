n,k = map(int,input().split())
a = list(map(int,input().split()))
a = [0]+a+[0]
i = j = 1
T = a[i]
lmin = n
while (i<=j) and (j<=n):
    if T<k :
        j += 1
        T += a[j]
    else: 
        lmin = min(lmin,j-i+1)
        T -= a[i]
        i += 1
print(lmin)