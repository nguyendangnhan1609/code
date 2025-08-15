d1 = d2 = d3 = 0
s = input()
for x in s:
    if (x=='C'): d1+=1 
    if (x=='O'): d2+=d1 
    if (x=='W'): d3+=d2 
print(d3)