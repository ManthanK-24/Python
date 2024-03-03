

n = int(input())
ar = list(map(int, input().strip().split()))

swaps = 0
for i in range(0, len(ar)):
    for j in range(0, len(ar)-1):
        if ar[j] > ar[j+1] :
            tmp = ar[j]
            ar[j] = ar[j+1]
            ar[j+1] = tmp
            swaps += 1
            
print("Array is sorted in", swaps, "swaps.")
print("First Element:", ar[0])
print("Last Element:", ar[n-1])
