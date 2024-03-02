

n = int(input())
ar = list(map(int, input().strip().split()))

mp = {}

for i in range(0, n):
    mp[ar[i]] = i

swaps = 0
for i in range(0, n):
    if (ar[i]!=i+1):
        tmp = mp[i+1]
        ar[tmp] = ar[i]
        mp[ar[i]] = tmp
        ar[i]=i+1
        mp[i+1] = i
        swaps += 1
print(swaps)        
