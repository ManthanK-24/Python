

n, k = map(int, input().split())
ar = list(map(int, input().strip().split()))
ar.sort()
toys = 0

for i in range(0, len(ar)):
    if (k>=ar[i]):
        k -= ar[i]
        toys += 1
    else:
        break 
print(toys)
