fi = open('cg.inp','r')
fo = open('cg.out','w')
n,k = map(int,fi.readline().split())
a = list(map(int,fi.readline().split()))
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
fo.write(str(lmin))
