
# write from scratch!

def solve(ls):
    
    ans = 0
    n = len(ls)
    for i in range(n-1, -1, -1):
        if (ls[i] - (i+1)> 2):
            print("Too chaotic")
            return
        for j in range(max(0, ls[i]-2), i):
            if (ls[j] > ls[i]):
                ans += 1
    print(ans)
        

t = int(input())
for tc in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    #print(type(ls))
    #print(ls)
    solve(ls)
