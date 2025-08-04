T1 = T2 = 1
j = 0
for i in range(1,3):
    S1,S2 = int,input()
    if S1 == 'END' and S2 == 'END':break;
    for i in len(S1):
        if S1[i] == S1[j]:
            T1 += 1
        j += 1
    j = 0
    for i in len(S2):
        if S2[i] == S2[j]:
            T2 += 1
    j += 1
if T1 == T2:
    print('same')
else:
    print('diffrent')