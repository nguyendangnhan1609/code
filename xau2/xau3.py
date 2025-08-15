# S = input()
# x = y =  o = 0
# for i in S:
#     while o = 0
#     if i == 'G':y += 1
#     if i == 'L':x -= 1
#     if i == 'R':x += 1
#     else: y -= 1
#     print(x,y)
    
L=[3,0,1,2]
R=[1,2,3,0]
B=[2,3,0,1]
tx=[0,1,0,-1]
ty=[1,0,-1,0]
n=int(input())
S=input()
x=y=0
h=0
for c in S:
    if c=='L': h=L[h]
    if c=='R': h=R[h]
    if c=='B': h=B[h]
    x+=tx[h]
    y+=ty[h]
print(x,y)