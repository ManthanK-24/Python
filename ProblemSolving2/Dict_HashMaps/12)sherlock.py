
q = int(input())
for t in range(0, q):
    s = input().strip()
    #print(s)
    count = 0
    substr = []
    for i in range(0, len(s)):
        sub = ""
        for j in range(i, len(s)):
            sub +=(s[j])
            substr.append(sub)
    pairs = []
    for x in substr:
        tmp = list(x)
        tmp.sort()
        tmp = str(tmp)
        pairs.append(tmp)
    mp = {}
    for x in pairs:
        if x in mp:
            mp[x] += 1
        else:
            mp[x] = 1
    for key, val in mp.items():
        
        count += (val*(val-1))//2
       
    print(count)
                                
            
            
        
            
