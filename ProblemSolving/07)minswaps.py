

n = int(input())
ls = list(map(int, input().split()))

mp = {}
for i in range(0, n):
    mp[ls[i]] = i

ans = 0

for i in range(0, n):
    ele = ls[i]
    if (ele!=i+1):
        mp[ls[i]] = mp[i+1]
        mp[i+1] = i
        ls[mp[ls[i]]] = ele
        ls[i] = i+1
        ans += 1
    #print(i, ans, ls)    
print(ans) 
