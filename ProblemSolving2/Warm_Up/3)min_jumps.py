
# if any whitespaces in input then strip to avoid

n = int(input())
# print(n)

ar = list(map(int, input().strip().split()))
#print(ar)

steps = 0
i = 0
while (i<len(ar)):
    if (i+1==n-1 or i+2==n-1):
        steps += 1
        break
    elif (ar[i+2]==0):
        steps += 1
        i=i+2
    elif (ar[i+1]==0):
        steps += 1
        i=i+1
print(steps)
    
    
