n = int(input())
a = [-1e9] + list(map(int, input().split())) + [1e9]
F = [0] * (n+3)
x = []
t = [0] * (n+3)
F[0] = 1
for i in range(1,n+2):
    for j in range(0,i):
        if (a[j] < a[i] and F[i] < F[j]+1):
            F[i] = F[j] + 1
            t[i] = j
print(F[n+1]-2)
m = n + 1
while m>0:
    x.append(a[m])
    m = t[m]
    x.pop(0)
for m in reversed(x): print(m,end=' ')