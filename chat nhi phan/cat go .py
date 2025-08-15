n,M = map(int,input().split())
a = list(map(int,input().split()))
def check(H):
    s = 0
    for x in a:
        if x>H: s += (x-H)
    if s >= M:return True
    else: return False

l = 0;r = max(a)
while l <= r:
    mid = (l+r)//2
    if check(mid):
        kq = mid
        l = mid + 1
    else:r = mid - 1
print(kq)