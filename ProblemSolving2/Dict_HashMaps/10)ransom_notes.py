
m, n = map(int, input().strip().split())
# print(m, n) 

maglis = input().strip().split()
# print(maglis)
magdict = {}
for x in maglis:
    if x in magdict:
        magdict[x] += 1
    else:
        magdict[x] = 1

notelis = input().strip().split()
# print(notelis)
flag = 1
for x in notelis:
    if x not in magdict:
        flag = 0
        break
    elif magdict[x]==0:
        flag=0
        break
    else:
        magdict[x] -= 1
if (flag==1):
    print("Yes")
else:
    print("No")

#print(maglis, notelis)
