n, s = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a
# Khởi tạo các mảng
f = [0] * (s + 1)
vet = [0] * (s + 1)
# Quy hoạch động
f[0] = 1
for i in range(1, n + 1):
    for j in range(s, a[i]-1, -1):
        if f[j - a[i]] == 1:
            f[j] = 1
            if vet[j] == 0: vet[j] = i
# Xuất kết quả
if f[s] == 0: print("NO")
else:
    print("YES")
    kq = []
    j = s
    while j > 0:
        kq.append(vet[j]) 
        j -= a[vet[j]]
    kq.reverse()  
    print(" ".join(map(str, kq)))
