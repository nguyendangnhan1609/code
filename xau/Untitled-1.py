def tanso(t):
    t = (0)*26
    for x in t:
        k = ord(x) - 97
        t[k] += 1
s1 = input()
s2 = input()
t1 = tanso(s1); t2 = tanso(s2)
for i in range(26):
    res += abs(t1[i] - t2[i])
print(res)