def dem_tan_so(s):
    s=s.replace(' ','')
    ts=[0]*26
    for x in s:
        k=ord(x)-97
        ts[k]+=1
    return ts
while (True):
    s1=input()
    s2=input()
    s1=s1.replace('\n','')
    s2=s2.replace('\n','')
    if s1=='END' and s2=='END': break
    a=dem_tan_so(s1)
    b=dem_tan_so(s2)
    if a==b: print('same')
    else: print('dif')
