

arr = []

for i in range(0, 6):
    arr.append(list(map(int, input().strip().split())))

#print(arr)

ans = -1000
for i in range(1, len(arr)-1):
    for j in range(1, len(arr)-1):
        val = arr[i][j] 
        val += arr[i-1][j]
        val += arr[i-1][j-1]
        val += arr[i-1][j+1]
        val += arr[i+1][j]
        val += arr[i+1][j-1]
        val += arr[i+1][j+1]
        ans = max(ans, val)
print(ans)
    
    
    
