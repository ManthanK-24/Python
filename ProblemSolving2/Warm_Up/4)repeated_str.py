

s = input().strip()
# print(s)
n = int(input())
# print(n)

times = s.count('a', 0, len(s))
#print(times)

ans = times*(n//len(s))
rem = n % len(s)
# print(ans, rem)
for i in range(rem):
    if (s[i]=='a'):
        ans += 1
print(ans)

