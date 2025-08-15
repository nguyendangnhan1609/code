# import sys
# sys.stdin = open("zxy.inp", "r")
# sys.stdout = open("zxy.out", "w")
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
def check(V):
    d = 1; s = 0
    for x in a:
        if s + x > V:
            d += 1#số thùng
            s = x
            if d > k:  # tối ưu: dừng sớm
                return False
        else:
            s += x
    return True
l = max(a)
r = sum(a)
res = r  # gán mặc định
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)