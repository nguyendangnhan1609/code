fi = open("./cploai.inp","r")
fo = open("cploai.out","w")
n = int(fi.readline())
arr = fi.readline()
arr = arr.split()
arr = map(int,arr)
arr = list(arr)
num = 0
for i in arr: 
    fo.write(str(i))
    num = num+1
    # if cploai.out 'đã có' i
    #    fo.write(' ')
    # else fo.write(str(i))
fo.write(str(num))   