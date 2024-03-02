
n = int(input())
# print(n)
ar = list(map(int, input().split()))
# print(ar)

freq = {}
for ele in ar:
    if (ele in freq):
        freq[ele] += 1
    else:
        freq[ele] = 1

ans = 0
for key, value in freq.items():
    ans += value//2
print(ans)
    
