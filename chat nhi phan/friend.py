n, B = map(int, input().split())
a = [int(input()) for _ in range(n)]
freq = {}
dem =   0
for val in a:
    need = B - val
    if need in freq:
        dem += freq[need]
    freq[val] = freq.get(val, 0) + 1
print(dem)