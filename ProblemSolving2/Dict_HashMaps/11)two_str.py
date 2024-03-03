
tc = int(input())
for t in range(0, tc):
    s1 = input().strip()
    s2 = input().strip()
    dsList = []
    flag = 0 
    for x in s1:
        if x not in dsList:
            dsList.append(x)
    for x in s2:
        if x in dsList:
            flag = 1
            break
    if (flag==1):
        print("YES")
    else:
        print("NO")
