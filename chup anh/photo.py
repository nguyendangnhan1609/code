n = int(input())
a = [(0,0)]
for i in range (n):
   x,y = map(int,input().split())
   a.append((x,y));
a = a+[(0,0)]
c = [0]*4
i = j = T =1
lmin = int(1e5)
c[a[1][1]] = 1
while i<=j and j<=n:
    if T<3:
        j += 1
        if c[a[j][1]] == 0: T += 1
        c[a[j][1]] += 1
    else:
        lmin = min(lmin , a[j][0]-a[i][0])
        c[a[i][1]] -= 1
        if c[a[i][1]] == 0: T -= 1
        i += 1
print(lmin)