
n, d = map(int, input().split())

#print(n, d)

ar = list(map(int, input().strip().split()))
ar = ar + ar
d = d % n
for i in range(d, d+n):
    print(ar[i], end=' ')
    
