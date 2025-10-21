strs=["bag","bag","bank","band"]
k=strs[0]
b=""
for i in range(1,len(strs)):
    p=0
    for j in range(len(k)):
        o=strs[j]
        o=o.split()
        if(k[p]==o[p]):
            b=b+k[p]
        p+=1
print(b)
