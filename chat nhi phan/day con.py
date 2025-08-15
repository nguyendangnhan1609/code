# import sys
# sys.fin
# sys.fout
n,s =map(int,input().split())
a = list(map(int,input().split()))
a=[0]+a
def check(mid):
    t = 0
    for i in range(1,mid+1):t += a[i]
    if t>=s:return True
    for i in range(mid+1,n+1):
        t += a[i]-a[i-mid]
        if t >= s: return True
    return False
l = 1;r = n
while l<=r:
    mid = (l+r)//2
    if check(mid):
        kq = mid 
        r = mid - 1
    else:l = mid + 1
print(kq)