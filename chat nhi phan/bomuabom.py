N,K = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
a_check = ''
for x in range(len(a)):
    a_check = a_check + (x)
print(a_check)
"""

def check(mid):
    

    return mid*2 < len(a) -1
                

l = 0;r = len(a) -1
while (l<=r):
    mid = (l+r)//2
    if (check(mid)):
        kq = mid
        l = mid + 1
    else:
        r = mid - 1
print(kq)

"""