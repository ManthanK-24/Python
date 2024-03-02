
n = int(input())
# print(n)
seq = input().strip()
# print(seq)

valleys = 0

level = 0

for i in range(0, len(seq)):
    if (seq[i]=='U'):
        level += 1
    else:
        level -= 1
    if (level==0 and seq[i]=='U'):
        valleys += 1
print(valleys)
