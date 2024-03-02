
t = int(input())
#print(t)
for tc in range(0, t):
    n = int(input())
    #print(n)
    ar = list(map(int, input().strip().split()))
    #print(ar)
    ans = 0
    chk = 1
    for i in range(1, n+1):
        dif = ar[i-1] - i
        if (dif>2):
            chk=0
            break
        elif (dif==2 ):
            ans += 1
    low = ar[n-1]
    for i in range(n-2, -1, -1):
        if (ar[i]>low):
            ans += 1
        low = min(ar[i], low)
            
    if (chk==1):
        print(ans)
    else:
        print("Too chaotic")  
        

